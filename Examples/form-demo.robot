*** Settings ***
Library    Dialogs    
Library    PuppeteerLibrary
Test Setup    Open browser to test page    
Test Teardown    Close Browser


*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/form.html


*** Test Cases ***
Select dropdown list by values with id
    Select From List By Value    id=cars    audi
    
Select dropdown list by values with xpath
    Select From List By Value    xpath=//select[@id="cars"]    audi

*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}

