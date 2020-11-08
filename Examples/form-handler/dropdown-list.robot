*** Settings ***
Library    PuppeteerLibrary
Test Setup    Open browser to test page
Test Teardown    Close All Browser
Suite Teardown    Close Puppeteer

*** Variables ***
${DEFAULT_BROWSER}    chrome
# ${DEFAULT_BROWSER}    webkit
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
    
Get selected dropdown list label
    Select From List By Label    id=cars    Audi
    ${Label} =    Get Selected List Label    xpath=//select[@id="cars"]
    Should Be Equal As Strings    Audi    ${Label}

Get selected dropdown list value
    Select From List By Label    id=cars    Audi
    ${Value} =    Get Selected List Value     xpath=//select[@id="cars"]
    Should Be Equal As Strings    audi    ${Value}

*** Keywords ***
Open browser to test page
    ${BROWSER} =     Get variable value    ${BROWSER}    ${DEFAULT_BROWSER}
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    ${HOME_PAGE_URL}    browser=${BROWSER}   options=${options}
