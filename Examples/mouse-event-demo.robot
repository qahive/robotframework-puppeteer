*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272


*** Test Cases ***
Mouse over event
    Run Async Keywords
    ...    Mouse Over    id=dropdown-menu    AND
    ...    Wait Until Element Is Visible    id=menu-docs    
    Click Element    id=menu-docs
    Wait Until Page Contains    This is a demo document content    


*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}

