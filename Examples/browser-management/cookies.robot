*** Settings ***
Library    PuppeteerLibrary
Suite Teardown    Close Puppeteer
Test Teardown    Close All Browser

*** Variables ***
${DEFAULT_BROWSER}    webkit


*** Test Cases ***
Get all cookies
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    https://www.blognone.com/    browser=${BROWSER}   options=${options}
    &{cookies} =    Get Cookies
    Should Not Be Empty    ${cookies}[_gat]
    
Get cookie
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    https://www.blognone.com/    browser=${BROWSER}   options=${options}
    ${cookie value} =    Get Cookie    _gat
    Should Not Be Empty    ${cookie value}
    
Add cookie
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    https://www.blognone.com/    browser=${BROWSER}   options=${options}
    Add Cookie    Test    1111
    &{cookies} =    Get Cookies
    Should Be Equal As Strings    1111    ${cookies}[Test]    

Delete all cookies
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}   options=${options}
    Delete All Cookies

    