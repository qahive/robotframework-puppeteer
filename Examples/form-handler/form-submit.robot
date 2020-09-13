*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/login-form-example.html


*** Test Cases ***
Submit login form
    Input Text    id=exampleInputEmail1    demo@qahive.com    
    Input Text    id=exampleInputPassword1    123456789
    Click Element    id=exampleCheck1
    Click Element    css=button[type="submit"]

*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}

