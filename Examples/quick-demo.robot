*** Settings ***
Library    PuppeteerLibrary

*** Test Cases ***
Control chrome browser
    [Teardown]    Close browser
    Open browser
    click_element    xxx
    
