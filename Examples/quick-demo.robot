*** Settings ***
Library    Dialogs
Library    PuppeteerLibrary

*** Test Cases ***
Control chrome browser
    [Teardown]    Test Teardown
    Open browser
    Input text    id=fname    demo-user
    Input text    id=fname    demo-usa
    
*** Keywords ***
Test Teardown
    Dialogs.Pause Execution
    Close browser
