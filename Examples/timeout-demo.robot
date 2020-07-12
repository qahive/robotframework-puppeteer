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
    Run Keyword And Expect Error    No new page has been open.*    Wait for new window open    1s
    Click Element    xpath://a[@href="docs.html"]
    Wait for new window open    5s
    

*** Keywords ***
Open test browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
    Maximize Browser Window
