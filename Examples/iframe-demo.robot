*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/iframe.html


*** Test Cases ***
Interact with iframe element
    Wait Until Page Contains Element    id=ifrm
    Select Frame    id=ifrm
    ${content} =    Get Text    id=container
    Should Contain    ${content}    Welcome Page    
    Unselect Frame
    ${content} =    Get Text    id=container
    Should Contain    ${content}    Demo iframe    

*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
