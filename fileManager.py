"""
Created by: Jesús Omar Cuenca Espino (JOmarCuenca)
jesomar.cuenca@gmail.com

26/03/2021
"""

import os
from shutil import rmtree

def createFolder(dirName : str, exists_ok = True):
    try:
        os.mkdir(dirName)
    except FileExistsError:
        print(f"Folder {dirName} already Exists")
    except FileNotFoundError:
        os.makedirs(dirName, exist_ok=exists_ok)

def deleteFolder(dirName : str):
    try:
        os.rmdir(dirName)
    except FileNotFoundError:
        print(f"Folder doesn't exist")
    except Exception as err:
        rmtree(dirName)

if __name__ == "__main__":
    import time
    TEST_DIR = SINGLE_DIR = "ExampleDir"
    createFolder(TEST_DIR)
    print("Folder Created")
    time.sleep(1)
    deleteFolder(TEST_DIR)
    print("Folder Deleted")

    TEST_DIR = "ExampleDir/InnerDir"
    createFolder(TEST_DIR)
    print("Inner Folder Created")
    time.sleep(1)
    deleteFolder(TEST_DIR)
    print("Inner Folder Deleted")
    deleteFolder(SINGLE_DIR)
    print("Upper Folder Deleted")
