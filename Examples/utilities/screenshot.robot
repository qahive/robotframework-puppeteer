*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Capture page screenshot
    Capture Page Screenshot
    Capture Page Screenshot    test-{index}.png
    Capture Page Screenshot    fullPage=True

Set page screenshot path
    Set Screenshot Directory    ./logs
    Capture Page Screenshot
    
Capture page screenshot should not run again if keyword failed
    Close All Browser
    Run Keyword And Expect Error    *    Capture Page Screenshot

*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}    options=${options}
