*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Mouse over event
    Run Async Keywords
    ...    Mouse Over    id=dropdown-menu    AND
    ...    Wait Until Element Is Visible    id=menu-login  
    Click Element    id=menu-login
    Wait Until Page Contains    Login form

Mouse drag
    [Tags]    Ignore_firefox    
    Mouse Down    id=ball
    Mouse Move    40    50
    Mouse Up        
   
Mouse drag and drop
    [Tags]    Ignore_firefox    Ignore_ptchrome
    Drag And Drop    id=ball    id=dropdown-menu
    
*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   browser=${BROWSER}    options=${options}
