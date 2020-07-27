*** Settings ***
Library    PuppeteerLibrary
Test Teardown    Close Browser


*** Test Cases ***
Example switch browser and browser title
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272   options=${options}
    Open browser    http://127.0.0.1:7272   options=${options}
    Maximize Browser Window
    ${title} =   Get title
    ${location} =   Get location
    Run Async Keywords    
    ...    Click Element    xpath://a[@href="docs.html"]    AND
    ...    Wait for new window open
    Switch Window   NEW
    ${Title} =   Get Title
    should be equal as strings  Docs Page   ${Title}
