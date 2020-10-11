*** Settings ***
Library    PuppeteerLibrary
Library    Dialogs    

*** Test Cases ***
New open browser
    [Teardown]    New Close Puppeteer
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    New Open Browser    https://www.google.com    browser=webkit    alias=B1    options=${options}
    Go To    https://www.youtube.com
    New Close Browser
