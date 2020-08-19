*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272


*** Test Cases ***
Switch to new tab by title with wait until keyword succeeds
    Click Link    id=readdocs
    Wait Until Keyword Succeeds    2x    2s    Switch Window    title=Docs Page
    
Switch to new tab by url with wait until keyword succeeds
    Click Link    id=readdocs
    Wait Until Keyword Succeeds    2x    2s    Switch Window    url=.*/docs.html$


*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}