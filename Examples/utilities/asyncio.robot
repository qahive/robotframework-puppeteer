*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Run Async Keywords and wait for first completed keyword
    ${result} =    Run Async Keywords And Return First Completed
    ...    Click Element    id=non_existing_id    AND
    ...    Click Element    id=get_ajax
    Run Keyword If    ${result} == 0    Log    first keyword pass
    Run Keyword If    ${result} == 1    Log    second keyword pass

*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
