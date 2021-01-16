*** Settings ***
Library    PuppeteerLibrary
Suite Teardown    Close Puppeteer
Test Teardown    Close All Browser

*** Variables ***
${DEFAULT_BROWSER}    chrome


*** Test Cases ***
Get all cookies
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    https://www.blognone.com/    browser=${BROWSER}   options=${options}
    &{cookies} =    Get Cookies
    Should Not Be Empty    ${cookies}[value]

Delete all cookies
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}   options=${options}
    Delete All Cookies

    