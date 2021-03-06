*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer


*** Variables ***
${DEFAULT_BROWSER}    pwchrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Generate pdf file
    [Tags]    Ignore_webkit    Ignore_firefox
    [Documentation]    Only support on chrome headless mode
    Print as pdf 


*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Set Variable    ${True}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}    options=${options}

