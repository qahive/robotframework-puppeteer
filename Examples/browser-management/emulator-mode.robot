*** Settings ***
Library    PuppeteerLibrary
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome
# ${DEFAULT_BROWSER}    webkit

*** Test Cases ***
Example enable emulator mode
    [Teardown]    Close All Browser
    ${BROWSER} =     Get variable value    ${BROWSER}     ${DEFAULT_BROWSER}
    ${HEADLESS} =    Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}    emulate=iPhone 11
    Open browser    http://127.0.0.1:7272/basic-html-elements.html   browser=${BROWSER}    options=${options}    alias=Browser 1
    Capture page screenshot
