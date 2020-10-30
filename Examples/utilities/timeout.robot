*** Settings ***
Force Tags    Ignore
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close Browser
Suite Teardown    Close Puppeteer


*** Variables ***
${DEFAULT_BROWSER}    chrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Default timeout
    Set Timeout    3s
    Run Keyword And Expect Error    No new page has been open.*    Wait for new window open
    
Timeout wait for new window open
    ${window count} =    Get Window Count
    Run Async Keywords
    ...    Wait for new window open    5s    AND    
    ...    Click Element    id:open-new-tab

*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}    options=${options}

