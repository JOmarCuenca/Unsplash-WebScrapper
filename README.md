# Unsplash-WebScrapper

This is a code designed to web scrap the website Unsplash.com using Selenium Web Driver.
It is intended to make easier the process of data collection for Neural Network and AI.
Or just if you need a bunch of images and you don't want to do it by hand.

- [Unsplash-WebScrapper](#unsplash-webscrapper)
  - [Usage with Examples](#usage-with-examples)
  - [Installation](#installation)
    - [Creating the Virtual Environment](#creating-the-virtual-environment)
    - [Getting the Selenium WebDriver](#getting-the-selenium-webdriver)
    - [Connecting the WebDriver to the code](#connecting-the-webdriver-to-the-code)
  - [Common Problems](#common-problems)

I took the time to implement a litte CLI functionallity.

## Usage with Examples

**Basic**
```python
    python3 imgScrapperUnsplash.py <<KEYWORD>>
```
**Target Amount**
```python
    python3 imgScrapperUnsplash.py <<KEYWORD>> --amount 70
```
**Target Amount and Divide into Train & Testing Set**
```python
    python3 imgScrapperUnsplash.py <<KEYWORD>> --amount 70 --divide 0.5
```

This will divide the downloaded images into 2 sets (Training & Testing), into the percentage sent as a CLI parameter.

**More info**
```python
    python3 imgScrapperUnsplash.py <<KEYWORD>> -h
```

## Installation

### Creating the Virtual Environment

Of course I left a **requirements.txt** file so you create a virtual environment first.

```bash
    python3 -m venv env
```

### Getting the Selenium WebDriver

And of course you'll need to have your selenium webdriver installed in your system before using this code. You can get a guide on how to install Selenium & get your driver [here](https://www.selenium.dev/documentation/getting_started/).

This code uses specifically Chrome, but feel free to tinker with it a little bit if you want to use something else.

### Connecting the WebDriver to the code

Next in order to make the code as fluid as possible I set it so you could write in a file named **pathFile.txt** with a single line with the absolute path to the webdriver so it is easy for the code to find.

However if you installed the driver somewhere easy to access and much rather write the path directly, you can also call the code as such:

**Specifying the Selenium Driver**
```python
    python3 imgScrapperUnsplash.py <<KEYWORD>> --path <<ABSOLUTE PATH TO DRIVER>>
```

## Common Problems

Due to the fact that Unsplash is a website which is continuously growing and changing it's HTML and CSS. It is quite possible for this webscrapper to become obsolete in the future. However the problem should be fixed quite easily by reconnecting the target HTML elements to the code.

I will personally attend every Issue posted in the Repo, after all it is my intention for this repo to be useful for the community. Also feel free to fork it or try to contribute to the repo. Just ask me first please.