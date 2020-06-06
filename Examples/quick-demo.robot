*** Settings ***
Library    PuppeteerLibrary

*** Test Cases ***
Example form control
    [Teardown]    Test Teardown
    Open browser
    Maximize Browser Window
    ${header} =    Get Text    css:h1
    ${fname} =    Get Value    id:fname
    Clear Element Text    id:fname
    Input text    id:fname    Mary
    Input text    xpath://input[@id="lname"]    Jane
    Click Element    xpath://input[@type="submit"]
    
Example specific element type click
    [Teardown]    Test Teardown
    Open browser
    Maximize Browser Window
    Click Link    partial link:Next

*** Keywords ***
Test Teardown
    Close browser
