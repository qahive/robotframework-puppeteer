*** Settings ***
Library    PuppeteerLibrary


*** Test Cases ***
Demo wait for element
    &{options} =    create dictionary   headless=${False}
    Open browser    https://www.w3schools.com/html/html_forms.asp   options=${options}
    Wait Until Page Contains Element    css:h1
    Run Keyword And Expect Error    STARTS: TimeoutError:    Wait Until Page Contains Element    css:no_element    timeout=5s
