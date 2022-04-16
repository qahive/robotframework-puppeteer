*** Settings ***
Library             PuppeteerLibrary

Suite Teardown      Close Puppeteer
Test Setup          Open browser to test page
Test Teardown       Close All Browser


*** Variables ***
${DEFAULT_BROWSER}      chrome
${HOME_PAGE_URL}        http://127.0.0.1:7272/basic-html-elements.html


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

Scroll element under iframe
    Wait Until Page Contains Element    id=ifrm2
    Select Frame    id=ifrm2
    Scroll Element Into View    id=exampleCheck1

Get text under iframe element
    Wait Until Page Contains Element    id=ifrm
    Select Frame    id=ifrm
    ${label text} =    Get Text    css=h2
    Should Be Equal As Strings    Login form    ${label text}
    ${label text} =    Get Text    xpath=//h2
    Should Be Equal As Strings    Login form    ${label text}

Get value under iframe element
    Wait Until Page Contains Element    id=ifrm
    Select Frame    id=ifrm
    Input Text    id=exampleInputEmail1    demo@qahive.com
    ${email value} =    Get Value    id=exampleInputEmail1
    Should Be Equal As Strings    demo@qahive.com    ${email value}


*** Keywords ***
Open browser to test page
    ${BROWSER} =    Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary    headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}    options=${options}
