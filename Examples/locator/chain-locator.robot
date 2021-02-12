*** Settings ***
Force Tags    Ingore_chrome
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    pwchrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/register-form-example.html


*** Test Cases ***
Chain css selector
    Input Text    chain=form >> input[type="email"]    Test

Chain xpath selector
    Input Text    chain=//form >> //input[@type="email"]    Test

Chain mix between xpath and css
    Input Text    chain=(//form)[1] >> input[type="email"]    Test            

*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}   options=${options}
