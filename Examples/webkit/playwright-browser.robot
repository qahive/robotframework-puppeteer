*** Settings ***
Library    PuppeteerLibrary
Library    Dialogs    

*** Test Cases ***
New open browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    New Open Browser    https://www.google.com    browser=webkit    alias=B1    options=${options}
    Dialogs.Pause Execution
    New Close Browser    
    # New Close All Browser
    New Close Puppeteer
    
    # New Open Browser    http://127.0.0.1:7272/basic-html-elements.html   options=${options}
    # Open Browser    http://127.0.0.1:7272/basic-html-elements.html   options=${options}
