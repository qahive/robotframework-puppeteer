[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/qahive/robotframework-puppeteer)

# robotframework-puppeteer
Robot Framework Puppeteer Library powered by [Pyppeteer](https://github.com/pyppeteer/pyppeteer). 
Improve automated web testing with native functionality from [Puppeteer](https://github.com/puppeteer/puppeteer) by Google.

More detail please visit [Robot Framework Puppeteer Homepage](https://qahive.github.io/robotframework-puppeteer.github.io/)

We aim to provide keywords similar to robotframework-seleniumlibrary and add core puppeteer functionality that will improve test experiences.
Example: 
- _Handle HTTP Request_
- _Handle HTTP Response_ 
- _Intercepter Http_
- _Intercepter javascript function_


Keyword documentation
---------------------
See [`keyword documentation`](https://qahive.github.io/robotframework-puppeteer/PuppeteerLibrary.html) for available keywords and more information about the library in general.



Installation
------------
The recommended installation method is using pip_::

    pip install --upgrade robotframework-puppeteerlibrary
    
Or manually install by running following command
    
    pip install -r requirements.txt
    python setup.py install


Usage
------------

    *** Settings ***
    Library    PuppeteerLibrary
    Test Teardown    Close Browser
    
    
    *** Test Cases ***
    Example login form submit
        ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
        &{options} =    create dictionary   headless=${HEADLESS}
        Open browser    http://127.0.0.1:7272   options=${options}
        Maximize Browser Window
        Input text    id:username_field    demo
        Input text    id:password_field    mode
        Click Element    id:login_button
        Wait Until Page Contains    Login succeeded
        # Logout and wait for homepage loaded
        Run Async Keywords
        ...    Click Link    partial link:logout    AND
        ...    Wait For Response Url    http://127.0.0.1:7272/
        
Please run demo application on your local before execute example test scripts.
        
**Starting demo application**

Running tests requires the demo application located under **demoapp** directory to be running. 
It can be started either by double clicking demoapp/server.py file in a file manager or by executing it from the command line:
    
    python demoapp/server.py

Full example please recheck [`Examples`](https://github.com/qahive/robotframework-puppeteer/tree/master/Examples)

Extended Puppeteer Libraries
------------

| Library        | Description |
| :---           | :---        |
| [Percy.io](https://github.com/qahive/robotframework-puppeteer-percy)  | Visual testing library for Robot Framework Puppeteer. |

Contributor
------------
robotframework-puppeteer mainly contribute by QAHive Co. Ltd.

Interested to contribute Cool!! please looking at the [Contribution guidelines](https://github.com/qahive/robotframework-puppeteer/blob/master/contributing.md)

Credit
------
  - [**robotframework-SeleniumLibrary**](https://github.com/robotframework/SeleniumLibrary): Keywords design and document content
  - [**robotframework-appiumlibrary**](https://github.com/serhatbolsu/robotframework-appiumlibrary): Keywords design and document content
  - [**demoapp**](https://github.com/robotframework/WebDemo): Clone from robotframework/WebDemo project
