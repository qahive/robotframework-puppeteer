# robotframework-puppeteer
Puppeteer with robotframework. This project connect between robotframework and puppeteer using [pyppeteer](https://github.com/pyppeteer/pyppeteer).

We aim for provide keyword similar to robotframework-seleniumlibrary and add core puppeteer functionality that will improve test experiences

Example: _Handle HTTP Request_, _Handle HTTP Response_ or _Intercepter http request & response_

Keyword documentation
---------------------
See [`keyword documentation`](https://qahive.github.io/robotframework-puppeteer/PuppeteerLibrary.html) for available keywords and more information about the library in general.



Installation
------------
The recommended installation method is using pip_::

    pip install --upgrade robotframework-puppeteer
    
Or manually install by running following command
    
    pip install -r requirements.txt
    python setup.py install


Usage
------------

    *** Settings ***
    Library    PuppeteerLibrary

    *** Test Cases ***
    Quick start with http request and response
        [Teardown]    Test Teardown
        &{options} =    create dictionary   headless=${False}
        Open browser    https://www.w3schools.com/js/js_ajax_intro.asp   options=${options}
        Run Async Keywords
        ...    Click Element    css:#demo button
        ...    AND    Wait for request url     https://www.w3schools.com/js/ajax_info.txt
        ...    AND    Wait for response url    https://www.w3schools.com/js/ajax_info.txt

    *** Keywords ***
    Test Teardown
        Close browser
        
Full example please recheck [`Examples`](https://github.com/qahive/robotframework-puppeteer/tree/master/Examples)


Contributor
------------
robotframework-puppeteer mainly contribute by QAHive Co. Ltd.

