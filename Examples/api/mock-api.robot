*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Mock ajax response with raw text
    &{response}    Create Dictionary    body=I'm a mock response text
    Mock Current Page Api Response    /ajax_info.json?count=3    ${response}        
    Click Element    id=get_ajax
    Wait Until Page Contains    I'm a mock response text
    
Mock ajax response with json response
    &{response}    Create Dictionary    body={ 'data': 'I\'m a mock response json'}    contentType=application/json
    Mock Current Page Api Response    /ajax_info.json?count=3    ${response}        
    Click Element    id=get_ajax
    Wait Until Page Contains    I'm a mock response json


*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}    options=${options}
