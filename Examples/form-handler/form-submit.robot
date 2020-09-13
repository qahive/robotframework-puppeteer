*** Settings ***
Library    PuppeteerLibrary
Test Teardown    Close Browser

*** Test Cases ***
Submit login form
    Open browser to test page    http://127.0.0.1:7272/login-form-example.html
    Input Text    id=exampleInputEmail1    demo@qahive.com
    Input Text    id=exampleInputPassword1    123456789
    Click Element    id=exampleCheck1
    Click Element    css=button[type="submit"]
    
Submit register form
    Open browser to test page    http://127.0.0.1:7272/register-form-example.html
    Input Text    id=inputEmail4    demo@qahive.com    
    Input Text    id=inputPassword4    123456789
    Input Text    id=inputAddress    123/234 wallstreet std.    
    Input Text    id=inputCity    Newyork
    Select From List By Value    id=inputState    5
    Input Text    id=inputZip    1234
    Click Element    css=button[type="submit"]

*** Keywords ***
Open browser to test page
    [Arguments]    ${url}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${url}   options=${options}
