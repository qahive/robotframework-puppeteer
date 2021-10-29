*** Settings ***
Library    PuppeteerLibrary
Suite Teardown    Close Puppeteer
Test Teardown    Close All Browser

*** Variables ***
${DEFAULT_BROWSER}    chrome


*** Test Cases ***
Get page title
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}   options=${options}
    ${title} =    Get Title
    Should Be Equal As Strings    Basic HTML Elements    ${title}

Get url
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html    browser=${BROWSER}   options=${options}
    ${url} =    Get Location
    Should Contain    ${url}    basic-html-elements.html
