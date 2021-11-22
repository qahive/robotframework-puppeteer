*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer


*** Variables ***
${DEFAULT_BROWSER}    chrome
${HOME_PAGE_URL}    https://demoqa.com/login
${PROFILE_PAGE_URL}    https://demoqa.com/profile
${USERNAME}    qahive
${PASSWORD}    Welcome1!


*** Test Cases ***
Save and Reuse browser authen state into json file
    [Tags]    Ignore_ptchrome
    Input Text    id=userName    ${USERNAME}
    Input Password    id=password    ${PASSWORD}
    Click Element    id=login
    Wait Until Page Contains Element    id=userName-value
    Wait Until Page Contains    ${USERNAME}    
    Save Browser Storage State    admin
    Close All Browser
    ############################################################
    # Reopen and bypass login by using state ref
    ############################################################
    ${BROWSER} =     Get variable value    ${BROWSER}     ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}    state_ref=admin
    Open browser    ${PROFILE_PAGE_URL}   browser=${BROWSER}    options=${options}
    Wait Until Page Contains    ${USERNAME}
    Delete Browser Storage State    admin
    Delete All Browser Storage States

*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}     ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   browser=${BROWSER}    options=${options}
    Set Screenshot Directory    test-report
    Capture Page Screenshot        
