*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
No node found when click
    Run Keyword And Expect Error    REGEXP:.*No node found for selector: #login_button_error    Click Element    id:login_button_error

Test log error for sync keywords
    Run Keyword And Ignore Error    Click Element    id:login_button_error

Test log error for async keywords
    Run Keyword And Ignore Error    Run Async Keywords    
    ...    Click Element    id:login_button_error    AND
    ...    Click Element    id:login_button_2

*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
