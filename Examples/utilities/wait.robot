*** Settings ***
Library    PuppeteerLibrary
Test Teardown    Close Browser

*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html
${LOGIN_PAGE_URL}    http://127.0.0.1:7272/login-form-example.html


*** Test Cases ***
Wait for element
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
    Wait Until Page Contains Element    id:get_ajax
    Run Keyword And Expect Error    STARTS: TimeoutError:    Wait Until Page Contains Element    css:no_element    timeout=5s

Wait for http request
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
    ${results} =    Run Async Keywords
    ...    Wait for request url     /ajax_info.json    AND
    ...    Click Element    id:get_ajax
    Should Contain    ${results[0].url}    ajax
    Should Be Equal As Strings    ${results[0].method}    GET
    Log    ${results[0].body}

Wait for http response
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
    ${results} =    Run Async Keywords
    ...    Wait for response url    /ajax_info.json\\?count=3    200    name.*?p1.*?name.*?p2.*?name.*?p3    AND
    ...    Click Element    id:get_ajax
    Should Contain    ${results[0].url}    ajax
    Should Be Equal As Strings    ${results[0].status}    200
    Log    ${results[0].body}

Wait for navigation
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
    Run Async Keywords
    ...    Wait For Navigation    AND
    ...    Click Element    id=goto-login-page

Wait for element hidden and visible
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
    Click Element    id:click_and_hide
    Wait Until Element Is Hidden    id:click_and_hide
    
Wait for element contains text
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${LOGIN_PAGE_URL}   options=${options}
    Wait Until Element Contains    id:emailHelp    We'll never share your email
    Wait Until Element Does Not Contains    id:emailHelp    We'll never share your password

Wait for location contains
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${LOGIN_PAGE_URL}   options=${options}
    Wait Until Location Contains    login-form-example.html

Wait for element is enabled
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
    Wait Until Element Is Enabled    id=prop-enable
    Click Element    id=prop-enable
