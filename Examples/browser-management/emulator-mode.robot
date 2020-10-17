*** Settings ***
Force Tags    Ignore
Library    PuppeteerLibrary
Suite Teardown    Close Puppeteer

*** Test Cases ***
Example enable emulator mode
    [Teardown]    Close All Browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272/basic-html-elements.html   options=${options}    alias=Browser 1
    Enable emulate mode    iPhone SE
    Capture page screenshot
