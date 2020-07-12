*** Settings ***
Library    PuppeteerLibrary
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272


*** Test Cases ***
Demo timeout wait for new window open
    Open browser    ${HOME_PAGE_URL}
    Maximize Browser Window
    Run Keyword And Expect Error    No new page has been open.*    Wait for new window open    1s
    Click Element    xpath://a[@href="docs.html"]
    Wait for new window open    5s
