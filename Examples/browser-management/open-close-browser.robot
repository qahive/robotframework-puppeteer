*** Settings ***
Library    PuppeteerLibrary
Suite Teardown    Close Puppeteer
Test Teardown    Close All Browser


*** Variables ***
${DEFAULT_BROWSER}    pwchrome


*** Test Cases ***
Open browser without option
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}

Open ssl issue page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary
    ...   headless=${HEADLESS}
    ...   ignore_https_errors=${True}
    ...   ignoreHTTPSErrors=${True}
    Open browser    https://expired.badssl.com/    browser=${BROWSER}   options=${options}
    Capture Page Screenshot

Switch to new browser
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}   options=${options}
    Run Async Keywords
    ...    Click Element    id=open-new-tab    AND
    ...    Wait For New Window Open
    Switch Window    NEW 
    Wait Until Page Contains Element    id=exampleInputEmail1
    Switch Window    title=Basic HTML Elements
    Wait Until Page Contains Element    id=open-new-tab    

Handle multiple browser    
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}    options=${options}    alias=Browser 1
    Run Async Keywords
    ...    Wait For New Window Open    AND
    ...    Click Element    id=open-new-tab
    Switch Window    NEW
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}    options=${options}    alias=Browser 2
    Switch Browser    Browser 1
    Wait Until Page Contains    Login form
    Switch Browser    Browser 2
    Wait Until Page Contains    Browser Management
    
Close current window
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}    options=${options}    alias=Browser 1
    Run Async Keywords
    ...    Wait For New Window Open    AND
    ...    Click Element    id=open-new-tab
    Switch Window    NEW    
    Wait Until Page Contains    Login form
    Close Window    

Window count
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}    options=${options}    alias=Browser 1
    ${no of window} =    Get Window Count
    Should Be Equal As Numbers    1    ${no of window}
    Run Async Keywords
    ...    Wait For New Window Open    AND
    ...    Click Element    id=open-new-tab
    ${no of window} =    Get Window Count
    Should Be Equal As Numbers    2    ${no of window}

Close browser before task finished should not throw error message
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${True}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}    options=${options}    alias=Browser 1
    Click Element    id=open-new-tab
    Click Element    id=open-new-tab
    Click Element    id=open-new-tab
    Click Element    id=open-new-tab
    Click Element    id=open-new-tab
    
Set view port
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}    options=${options}
    Set View Port Size    200    200
