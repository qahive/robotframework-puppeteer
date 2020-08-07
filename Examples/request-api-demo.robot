*** Settings ***
Library    Dialogs    
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272


*** Test Cases ***
Mock response for api request
    &{response}    Create Dictionary    body=I'm a mock response
    Mock Current Page Api Response    /ajax_info.json\\?count=3    ${response}        
    Click Element    id=get_ajax
    Wait Until Page Contains    I'm a mock response
    
Mock response with json response
    &{response}    Create Dictionary    body={ 'data': 'I\'m a mock response'}    contentType=application/json
    Mock Current Page Api Response    /ajax_info.json\\?count=3    ${response}        
    Click Element    id=get_ajax
    Wait Until Page Contains    I'm a mock response    
    
*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
