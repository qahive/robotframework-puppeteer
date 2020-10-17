*** Settings ***
Force Tags    Ignore
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html

*** Test Cases ***
Accept alert
    Run Async Keywords
    ...    Handle Alert    ACCEPT    AND
    ...    Click Button    id=alert_confirm
    Click Element    id:get_ajax

Dismiss alert
    Run Async Keywords
    ...    Handle Alert    DISMISS    AND
    ...    Click Button    id=alert_confirm
    Click Element    id:get_ajax
    
*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}

