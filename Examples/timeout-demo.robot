*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open test browser
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272


*** Test Cases ***
Set default timeout
    Set Timeout    3s
    Run Keyword And Expect Error    No new page has been open.*    Wait for new window open
    
Timeout wait for new window open
    Run Async Keywords
    ...    Wait for new window open    5s    AND
    ...    Click Element    id:readdocs

*** Keywords ***
Open test browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
    Maximize Browser Window
