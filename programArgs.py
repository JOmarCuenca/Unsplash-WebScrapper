import argparse

class ProgramArgs:

    def __init__(self, keyword : str, targetNum : int, path : str, divide : float) -> None:
        self.keyword    = keyword
        self.targetNum  = targetNum
        self.path       = path
        self.divide     = divide

def getArgs():
    parser = argparse.ArgumentParser(description='Program to collect images from Unsplash.com using Selenium.')
    parser.add_argument('keyword', type=str, help='Keyword to look for in Unsplash.com, like the one used on the searchbar.')
    parser.add_argument("--amount", nargs="?", default=100, type=int, help="Amount of Images to try to collect from the website. Defaults to 100.")
    parser.add_argument("--divide", nargs="?", const=0.8, type=float, help="Percentage of Divison into test and train values. If used defaults to 0.8.")
    parser.add_argument("-p", "--path", dest="path", nargs="?", help="Explicit PATH to the selenium WebDriver")
    rawArgs = parser.parse_args()
    return ProgramArgs(rawArgs.keyword, rawArgs.amount, rawArgs.path, rawArgs.divide)

if __name__ == "__main__":
    temp = getArgs()
    print(f"Keyword >> {temp.keyword}")
    print(f"TargetNum >> {temp.targetNum}")
    print(f"Divide >> {temp.divide}")
    print(f"Path >> {temp.path}")
    