*** Settings ***
Library    PuppeteerLibrary

*** Test Cases ***
Example browser title
    [Teardown]    Test Teardown
    Open browser    https://www.w3schools.com/html/html_forms.asp
    Maximize Browser Window
    ${title} =   Get title
    Click Link    partial link:Next

*** Keywords ***
Test Teardown
    Close browser
