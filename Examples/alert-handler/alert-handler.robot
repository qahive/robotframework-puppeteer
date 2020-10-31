*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer


*** Variables ***
${DEFAULT_BROWSER}    chrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Accept alert
    [Tags]    Ignore_webkit    Ignore_firefox
    Run Async Keywords
    ...    Handle Alert    ACCEPT    AND
    ...    Click Element    id=alert_confirm
    Click Element    id:get_ajax

Dismiss alert
    [Tags]    Ignore_webkit    Ignore_firefox
    Run Async Keywords
    ...    Handle Alert    DISMISS    AND
    ...    Click Element    id=alert_confirm
    Click Element    id:get_ajax

    
*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}     ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   browser=${BROWSER}    options=${options}
