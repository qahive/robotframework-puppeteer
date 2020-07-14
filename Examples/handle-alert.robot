*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272


*** Test Cases ***
Accept Handle alert
    Run Async Keywords
    ...    Handle Alert    ACCEPT    AND
    ...    Click Button    id=alert_confirm
    Click Element    id:get_ajax

Dismiss Hadle alert
    Run Async Keywords
    ...    Handle Alert    DISMISS    AND
    ...    Click Button    id=alert_confirm
    Click Element    id:get_ajax


*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
