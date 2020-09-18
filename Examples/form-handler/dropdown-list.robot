*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${HOME_PAGE_URL}    http://127.0.0.1:7272/basic-html-elements.html


*** Test Cases ***
Select dropdown list by values with id
    Select From List By Value    id=cars    audi
    
Select dropdown list by values with xpath
    Select From List By Value    xpath=//select[@id="cars"]    audi
    
Select dropdown list by labels with id
    Select From List By Label    id=cars    Audi
    
Select dropdown list by labels with xpath
    Select From List By Label    xpath=//select[@id="cars"]    Audi   

*** Keywords ***
Open browser to test page
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}   options=${options}
