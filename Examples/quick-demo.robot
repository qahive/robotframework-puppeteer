*** Settings ***
Library    PuppeteerLibrary

*** Test Cases ***
Control chrome browser
    [Teardown]    Test Teardown
    Open browser
    Maximize Browser Window
    Input text    id=fname    Mary
    Input text    xpath=//input[@id="lname"]    Jane
    Click Element    xpath=//input[@type="submit"]

*** Keywords ***
Test Teardown
    Close browser
