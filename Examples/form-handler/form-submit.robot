*** Settings ***
Library    PuppeteerLibrary
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    webkit


*** Test Cases ***
Submit login form
    Open browser to test page    http://127.0.0.1:7272/login-form-example.html
    Input Text    id=exampleInputEmail1    demo@qahive.com
    Input Text    xpath=//*[@id='exampleInputPassword1']    123456789
    Click Element    id=exampleCheck1
    Run Async Keywords
    ...    Wait For New Window Open    AND
    ...    Click Element    css=button[type="submit"]
    Switch Window    NEW
    Wait Until Page Contains    Login succeeded
    
Submit register form
    Open browser to test page    http://127.0.0.1:7272/register-form-example.html
    Input Text    id=inputEmail4    demo@qahive.com    
    Input Text    id=inputPassword4    123456789
    Input Text    id=inputAddress    123/234 wallstreet std.    
    Input Text    id=inputCity    Newyork
    Select From List By Value    id=inputState    5
    Input Text    id=inputZip    1234
    Click Element    css=button[type="submit"]

Webkit demo skip wait after click
    [Tags]    Ignore
    Open browser to test page    https://www.w3schools.com/html/html_forms.asp
    Wait Until Element Is Visible    id=fname
    Input Text     id=fname     123
    Input Text     id=lname     321
    Run Async Keywords
    ...    Wait For New Window Open    AND
    ...    Click Element     xpath=(//input[@value="Submit"])[1]    ${True}
    Switch Window    NEW
    Wait Until Page Contains    Submitted Form Data

*** Keywords ***
Open browser to test page
    [Arguments]    ${url}
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${url}    browser=${BROWSER}   options=${options}
