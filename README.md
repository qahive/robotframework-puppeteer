# robotframework-puppeteer
Puppeteer with robotframework. This project connect between robotframework and puppeteer using [pyppeteer](https://github.com/pyppeteer/pyppeteer).


Keyword documentation
---------------------
See `keyword documentation` for available keywords and more information
about the library in general.


Installation
------------
The recommended installation method is using pip_::

    pip install --upgrade robotframework-puppeteer
    
Or manuall install by running following command
    
    pip install -r requirements.txt
    python setup.py install

Usage
------------

    *** Settings ***
    Library    PuppeteerLibrary

    *** Test Cases ***
    Control chrome browser
        [Teardown]    Test Teardown
        Open browser
        Maximize Browser Window
        Input text    id=fname    Mary
        Input text    id=lname    Jane
        Click Element    css=input[type=submit]

    *** Keywords ***
    Test Teardown
        Close browser
