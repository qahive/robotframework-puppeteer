*** Settings ***
Library    Dialogs
Library    PuppeteerLibrary

*** Test Cases ***
Control chrome browser
    [Teardown]    Test Teardown
    Open browser
    Maximize Browser Window
    Input text    id=fname    Mary
    Input text    id=lname    Jane
    Click Element    css=input[type=submit]

*** Keywords ***
Test Teardown
    Dialogs.Pause Execution
    Close browser
