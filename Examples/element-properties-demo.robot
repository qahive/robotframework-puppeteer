*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272


*** Test Cases ***
Element property is disable
    Element Should Be Disabled    id:disabled-button
    Run Keyword And Expect Error    REGEXP:Element 'id:username_field' is enabled    Element Should Be Disabled    id:username_field

Element proprty is enable
    Element Should Be Enabled    id:username_field

*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
