*** Settings ***
Library    PuppeteerLibrary
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome


*** Test Cases ***
Click link
    Open browser to test page    http://127.0.0.1:7272/basic-html-elements.html
    Click Link    id=goto-login-page
    
Click Button
    Open browser to test page    http://127.0.0.1:7272/basic-html-elements.html
    Click Button    id=get_ajax

Double Click Element
    Open browser to test page    http://127.0.0.1:7272/basic-html-elements.html
    Double Click Element    id=double_click_get_id

Click Image
    Open browser to test page    http://127.0.0.1:7272/basic-html-elements.html
    Click Image    id=gate

Click element at coordiator
    Open browser to test page    http://127.0.0.1:7272/login-form-example.html
    Run Async Keywords
    ...    Wait For New Window Open    AND
    ...    Click Element At Coordinate    css=button[type="submit"]    1    1

*** Keywords ***
Open browser to test page
    [Arguments]    ${url}
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${url}    browser=${BROWSER}   options=${options}
