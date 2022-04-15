*** Settings ***
Library           PuppeteerLibrary
Test Setup        Open browser to test page
Test Teardown     Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html

*** Test Cases ***
No node found when click
    Set Timeout    2s
    Run Keyword And Expect Error    REGEXP:.*    Click Element    id:login_button_error

Test log error for sync keywords
    Run Keyword And Ignore Error    Click Element    id:login_button_error

Test log error for async keywords
    Run Keyword And Ignore Error    Run Async Keywords
    ...    Click Element    id:login_button_error    AND
    ...    Click Element    id:login_button_2

*** Keywords ***
Open browser to test page
    ${BROWSER} =    Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${True}
    &{options} =    create dictionary    headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}    options=${options}
