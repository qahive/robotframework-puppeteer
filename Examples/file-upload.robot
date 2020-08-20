*** Settings ***
Library    PuppeteerLibrary    
Test Setup    Open browser to test page    
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/file-upload.html


*** Test Cases ***
Upload file demo
    Upload file    id=fileToUpload    ${CURDIR}/quick-start.robot


*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
