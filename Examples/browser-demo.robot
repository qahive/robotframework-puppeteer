*** Settings ***
Library    PuppeteerLibrary


*** Test Cases ***
Example switch window and check window title
    [Teardown]    Close Browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272   options=${options}
    Maximize Browser Window
    ${title} =   Get title
    ${location} =   Get location
    Run Async Keywords
    ...    Wait for new window open    AND
    ...    Click Element    xpath://a[@href="docs.html"]
    Switch Window   NEW
    ${Title} =   Get Title
    should be equal as strings  Docs Page   ${Title}

Example open multiple browser
    [Teardown]    Close All Browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272   options=${options}    alias=Browser 1
    Click Element    id=login_button
    Open browser    http://127.0.0.1:7272   options=${options}    alias=Browser 2
    Click Element    id=get_ajax
    Switch Browser    Browser 1
    Wait Until Page Contains    Error Page    
    Switch Browser    Browser 2
    Wait Until Page Contains    products

Example close puppeteer browser
    [Teardown]    Close All Browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272   options=${options}    alias=Browser 1
    Close Puppeteer
    Open browser    http://127.0.0.1:7272   options=${options}    alias=Browser 2
    Click Element    id=get_ajax
