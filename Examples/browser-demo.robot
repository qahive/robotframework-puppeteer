*** Settings ***
Library    PuppeteerLibrary
Library    Dialogs

*** Test Cases ***
Example browser title
    [Teardown]    Test Teardown
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    https://www.w3schools.com/html/html_forms.asp   options=${options}
    Maximize Browser Window
    ${title} =   Get title
    ${location} =   Get location
    Click Element    xpath://*[@id="main"]/div[3]/div/form/input[3]
    Wait for new window open
    Switch Window   NEW
    ${Title} =   Get Title
    should be equal as strings  Forms action page   ${Title}


*** Keywords ***
Test Teardown
    Close browser
