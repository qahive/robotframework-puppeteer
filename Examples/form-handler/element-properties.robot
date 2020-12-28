*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Count element
    ${No of h2} =    Get Element Count    css=h2
    Should Be Equal As Numbers    13    ${No of h2}

Get element attribute
    ${type value} =   Get Element Attribute    id=alert_confirm    type
    Should Be Equal As Strings    button    ${type value}

Element proprty is enable
    Element Should Be Enabled    id:prop-enable

Element property is disable
    Element Should Be Disabled    id:prop-disable
    Run Keyword And Expect Error    REGEXP:Element 'id:prop-enable' is enabled    Element Should Be Disabled    id:prop-enable
    
Element is visible and not visible
    [Tags]    Ignore_firefox
    #TODO Need to recheck why firefox unstable
    Element Should Be Visible    id:prop-visible
    Element Should Not Be Visible    id:prop-hide
    Run Keyword And Expect Error    REGEXP:Element 'id:prop-hide' is not be visible    Element Should Be Visible    id:prop-hide

Get Element Text
    ${text} =    Get Text    id=prop-text    
    Should Contain    ${text}    Please

Element should containt text
    Element Should Contain    id=prop-text    Please    ${True}
    
Element should not contain text
    Element Should Not Contain    id=prop-text    Please input2    ${True}
    
Element text should be
     Element Text Should Be    id=prop-text    Please input    ${True}
     
Element text should not be
    Element Text Should Not Be    id=prop-text    Please    ${True}    

*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}   options=${options}
