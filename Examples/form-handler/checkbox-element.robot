*** Settings ***
Library    PuppeteerLibrary
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome


*** Test Cases ***
Select Checkbox element 
    Open browser to test page    http://127.0.0.1:7272/login-form-example.html
    Select Checkbox    id=exampleCheck1
    Checkbox Should Be Selected    id=exampleCheck1
    
Unselect Checkbox element
    Open browser to test page    http://127.0.0.1:7272/login-form-example.html
    Select Checkbox    id=exampleCheck1
    Unselect Checkbox    id=exampleCheck1
    Checkbox Should Not Be Selected    id=exampleCheck1
    


*** Keywords ***
Open browser to test page
    [Arguments]    ${url}
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${url}    browser=${BROWSER}   options=${options}
