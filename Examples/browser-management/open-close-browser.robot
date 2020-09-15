*** Settings ***
Library    PuppeteerLibrary
Suite Teardown    Close Puppeteer

*** Test Cases ***
Switch to new browser
    &{options} =    create dictionary   headless=${False}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html   options=${options}
    Run Async Keywords
    ...    Wait For New Window Open    AND
    ...    Click Element    id=open-new-tab
    Switch Window    NEW
    Wait Until Page Contains Element    id=exampleInputEmail1
    Switch Window    title=Basic HTML Elements
    Wait Until Page Contains Element    id=open-new-tab    
    Close All Browser
