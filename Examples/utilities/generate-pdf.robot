*** Settings ***
Force Tags    Ignore
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer


*** Variables ***
${DEFAULT_BROWSER}    chrome
# ${DEFAULT_BROWSER}    webkit
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Generate pdf file
    [Documentation]    Only support on headless mode
    Print as pdf 


*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}    options=${options}

