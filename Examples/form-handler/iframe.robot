*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Interact with iframe element
    Wait Until Page Contains Element    id=ifrm
    Select Frame    id=ifrm
    # Input Text not support iframe
    # Input Text    id=exampleInputEmail1    demo@qahive.com
    # Input Text    id=exampleInputPassword1    123456789
    Click Element    id=exampleCheck1
    
*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
