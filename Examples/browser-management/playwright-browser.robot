*** Settings ***
Library    PuppeteerLibrary

*** Test Cases ***
New open browser
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    New Open Browser    http://127.0.0.1:7272/basic-html-elements.html   options=${options}
