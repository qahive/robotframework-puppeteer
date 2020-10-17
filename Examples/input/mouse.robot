*** Settings ***
Force Tags    Ignore
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close All Browser

*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Mouse over event
    Run Async Keywords
    ...    Mouse Over    id=dropdown-menu    AND
    ...    Wait Until Element Is Visible    id=menu-login  
    Click Element    id=menu-login
    Wait Until Page Contains    Login form

Mouse drag
    Mouse Down    id=ball
    Mouse Move    40    50
    Mouse Up        

*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}

