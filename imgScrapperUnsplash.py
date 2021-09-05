"""
Created by Jesús Omar Cuenca Espino (JOmarCuenca)
jesomar.cuenca@gmail.com

26/03/2021
"""
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
import time
from fileManager import createFolder,deleteFolder
import programArgs as pargs
from progressbar import progressbar, streams
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Setup Progressbar wrapper function
streams.wrap_stderr()

_DEFAULT_SEPARATOR_LENGTH = 50
_WEBSITE_URL = "https://unsplash.com"
_imgURL = []

def printSeparator(title : str, length = _DEFAULT_SEPARATOR_LENGTH):
    """
    Prints a separator in console to visualize better the sections of the code.

    Args:
        title (str): Title of the separator
        length (int, optional): Length of the separator. Defaults to DEFAULT_SEPARATOR_LENGTH.
    """
    logger.info(f" {title.upper()} ".center(length,'='))

def getURLs(images):
    """
    Gets the URL's of the images to be downloaded from the website according to the website design.

    Args:
        images (List[str]): Array of HTML Attr with the target http link of the imgs.
    """
    printSeparator("Getting imgs URL's current screen")
    for img in images:
        srcset = img.get_attribute("srcset")
        if(srcset == None):
            continue
        sources = srcset.split(" ")
        for src in sources:
            if("http" in src and "fit=crop&w=700" in src):
                _imgURL.append(src)

def cleanDuplicates():
    """
    Cleans possible duplicate urls.
    """
    global _imgURL
    _imgURL = list(dict.fromkeys(_imgURL))

def writeImgs(urls : list, trainPath : str, testPath : str = None, proportion : float = None):
    """
    Saves the PNG files in the targeted dirs from the collected URLS.

    Args:
        urls (list): Targeted URL's of the img files
        trainPath (str): Training dir path
        testPath (str): Testing dir path
    """
    targetFolder = trainPath
    switch = False
    printSeparator("Saving Imgs")
    for x in progressbar(range(len(urls))):
        if(not switch and testPath != None and proportion != None and x > len(urls) * proportion):
            switch = True
            targetFolder = testPath
        webImg = requests.get(urls[x])
        f = open(f"./{targetFolder}img_{x + 1}.png","wb")
        f.write(webImg.content)
        f.close()

def mainActivity(driver, currentHeight, targetNumImgs):
    global _imgURL
    # Get scroll height
    last_height = currentHeight
    new_height  = -1
    iters = 0
    toBottom = False
    while len(_imgURL) < targetNumImgs and iters < 20:
        # Wait to load page
        time.sleep(1)

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*31/33);" if toBottom else "window.scrollTo(0, document.body.scrollHeight*9/11);")

        # Wait to load page
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        images = driver.find_elements_by_class_name("oCCRx")

        getURLs(images)
        cleanDuplicates()

        iters += 1

        if new_height == last_height:
            logger.warning("Height didn't update")
            if(toBottom):
                break
            else:
                toBottom = True
        last_height = new_height


if __name__ == "__main__":
    args = pargs.getArgs()
    openBrowser = True
    path = args.path

    driver : WebDriver = None
    
    if(path is None):
        try:
            with open("pathFile.txt","r") as pathFile:
                path = pathFile.readline().rstrip()
                pathFile.close()
        except Exception:
            openBrowser = False

    driver = Chrome(path)

    driver.get(_WEBSITE_URL)
    searchBar = driver.find_element_by_name("searchKeyword")

    try:
        if not openBrowser:
            raise Exception("No path to the selenium web driver")
        searchBar.send_keys(args.keyword)
        searchBar.send_keys(Keys.ENTER)
    except IndexError:
        openBrowser = False
        driver.close()

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    if(openBrowser):

        mainFolder = f"data/{args.keyword}/"
        trainFolder = None
        testFolder  = None

        if(args.divide != None):
            trainFolder = f"{mainFolder}train/"
            testFolder  = f"{mainFolder}test/"

            ## Delete existing folders, if any
            deleteFolder(trainFolder)
            deleteFolder(testFolder)

            ## Create Folders
            createFolder(trainFolder)
            createFolder(testFolder)

        else:
            # Delete folder if exists
            deleteFolder(mainFolder)

            # Create Folder
            createFolder(mainFolder)

        mainActivity(driver, last_height, args.targetNum)

        driver.close()

        if(args.divide != None):
            writeImgs(_imgURL,trainFolder,testFolder, proportion=args.divide)
        else:
            writeImgs(_imgURL,mainFolder)
