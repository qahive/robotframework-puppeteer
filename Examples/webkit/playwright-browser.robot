*** Settings ***
Library    PuppeteerLibrary
Library    Dialogs    

*** Test Cases ***
New open browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    New Open Browser    https://www.google.com    browser=webkit   options=${options}
    Dialogs.Pause Execution
    # New Open Browser    http://127.0.0.1:7272/basic-html-elements.html   options=${options}
    # Open Browser    http://127.0.0.1:7272/basic-html-elements.html   options=${options}
