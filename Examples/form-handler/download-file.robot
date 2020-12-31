*** Settings ***
Library    OperatingSystem
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Download file  
    ${file path} =    Download File    id=download-file
    Should Not Be Empty    ${file path}    Download file failed
    Get File    ${file path}    
    
Upload file
    Upload File    id=fileToUpload    ${CURDIR}\\iframe.robot

*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}   options=${options}
