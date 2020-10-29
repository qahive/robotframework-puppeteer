*** Settings ***
Force Tags    Ignore
Library    Dialogs    
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
# ${DEFAULT_BROWSER}    chrome
${DEFAULT_BROWSER}    webkit
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Run Async Keywords and wait for first completed keyword
    ${result} =    Run Async Keywords And Return First Completed
    ...    Click Element    id=non_existing_id    AND
    ...    Click Element    id=get_ajax
    Should Be Equal As Integers    1    ${result}
    Run Keyword If    ${result} == 0    Log    first keyword completed
    Run Keyword If    ${result} == 1    Log    second keyword completed
    
Ignore error Run Async Keywords and Return First Complete if no keyword success
    Run Keyword And Expect Error    All async keywords failed*    Run Async Keywords And Return First Completed
    ...    Click Element    id=non_existing_id    AND
    ...    Click Element    id=non_existing_id2

*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}    options=${options}
