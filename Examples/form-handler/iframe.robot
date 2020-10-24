*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer


*** Variables ***
# ${DEFAULT_BROWSER}    chrome
${DEFAULT_BROWSER}    webkit
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Interact with iframe element
    Wait Until Page Contains Element    id=ifrm
    Select Frame    id=ifrm
    Input Text    id=exampleInputEmail1    demo@qahive.com
    Input Text    xpath=//*[@id='exampleInputPassword1']    123456789
    Click Element    id=exampleCheck1
    Click Element    xpath=//*[@id='exampleCheck1']
    Unselect Frame
    Wait Until Page Contains Element    id=ifrm
    
*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary    headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}    options=${options}
