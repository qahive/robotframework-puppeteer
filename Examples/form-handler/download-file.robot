*** Settings ***
Library    OperatingSystem
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer


*** Variables ***
${DEFAULT_BROWSER}    pwchrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Download file
    ${file path} =    Download File    id=download-file
    Wait Until Keyword Succeeds    3x    2s    Copy File    ${file path}    test.csv   
    Get File    test.csv
    
Upload file
    ${file} =    OperatingSystem.Join Path    ${CURDIR}    iframe.robot
    Upload File    id=fileToUpload    ${file}

*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}   options=${options}
