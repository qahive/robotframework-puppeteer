*** Settings ***
Force Tags    Ignore
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Generate pdf file
    [Documentation]    Only support on headless mode
    Print as pdf 

*** Keywords ***
Open browser to test page
    &{options} =    create dictionary   headless=${True}
    Open browser    ${HOME_PAGE_URL}   options=${options}
