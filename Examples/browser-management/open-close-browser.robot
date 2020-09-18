*** Settings ***
Library    PuppeteerLibrary
Suite Teardown    Close Puppeteer
Test Teardown    Close All Browser

*** Test Cases ***
Switch to new browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${False}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html   options=${options}
    Run Async Keywords
    ...    Wait For New Window Open    AND
    ...    Click Element    id=open-new-tab
    Switch Window    NEW
    Wait Until Page Contains Element    id=exampleInputEmail1
    Switch Window    title=Basic HTML Elements
    Wait Until Page Contains Element    id=open-new-tab    

Handle multiple browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html   options=${options}    alias=Browser 1
    Run Async Keywords
    ...    Wait For New Window Open    AND
    ...    Click Element    id=open-new-tab
    Switch Window    NEW
    Open browser    http://127.0.0.1:7272/basic-html-elements.html   options=${options}    alias=Browser 2
    Switch Browser    Browser 1
    Wait Until Page Contains    Login form
    Switch Browser    Browser 2
    Wait Until Page Contains    Browser Management
    