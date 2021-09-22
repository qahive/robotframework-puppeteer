*** Settings ***
Library    PuppeteerLibrary
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    pwchrome


*** Test Cases ***
Tracing log without path
    Open browser to test page    http://127.0.0.1:7272/login-form-example.html
    Start tracing
    Select Checkbox    id=exampleCheck1
    Checkbox Should Be Selected    id=exampleCheck1
    Stop Tracing    

*** Keywords ***
Open browser to test page
    [Arguments]    ${url}
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${url}    browser=${BROWSER}   options=${options}
