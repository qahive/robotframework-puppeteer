*** Settings ***
Library    PuppeteerLibrary
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome


*** Test Cases ***
Tracing log without path
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    Open browser to test page    http://127.0.0.1:7272/login-form-example.html
    Run Keyword If    '${BROWSER}' != 'ptchrome'    Start tracing    
    Select Checkbox    id=exampleCheck1
    Checkbox Should Be Selected    id=exampleCheck1
    Run Keyword If    '${BROWSER}' != 'ptchrome'    Stop Tracing

Tracing log with specific path
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    Open browser to test page    http://127.0.0.1:7272/login-form-example.html
    Run Keyword If    '${BROWSER}' != 'ptchrome'    Start tracing    
    Select Checkbox    id=exampleCheck1
    Checkbox Should Be Selected    id=exampleCheck1
    Run Keyword If    '${BROWSER}' != 'ptchrome'    Stop Tracing    trace2.zip

*** Keywords ***
Open browser to test page
    [Arguments]    ${url}
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${url}    browser=${BROWSER}   options=${options}
