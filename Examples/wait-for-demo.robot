*** Settings ***
Library    Dialogs    
Library    PuppeteerLibrary
Test Teardown    Close Browser


*** Test Cases ***
Demo wait for element
    &{options} =    create dictionary   headless=${False}
    Open browser    https://www.w3schools.com/html/html_forms.asp   options=${options}
    Wait Until Page Contains Element    css:h1
    Run Keyword And Expect Error    STARTS: TimeoutError:    Wait Until Page Contains Element    css:no_element    timeout=5s

Demo wait for http response
    &{options} =    create dictionary   headless=${False}
    Open browser    https://www.w3schools.com/js/js_ajax_intro.asp   options=${options}
    Click Element    css:#demo button
    Wait for response url    https://www.w3schools.com/js/ajax_info.txt

Demo wait for http request and response
    &{options} =    create dictionary   headless=${False}
    Open browser    https://www.w3schools.com/js/js_ajax_intro.asp   options=${options}
    Run Async Keywords
    ...    Click Element    css:#demo button
    ...    AND    Wait for request url     https://www.w3schools.com/js/ajax_info.txt
    ...    AND    Wait for response url    https://www.w3schools.com/js/ajax_info.txt
    
Demo wait for navigation
    &{options} =    create dictionary   headless=${False}
    Open browser    https://www.w3schools.com/js/js_ajax_intro.asp   options=${options}
    Run Async Keywords
    ...    Click Link    partial link:Next
    ...    AND    Wait For Navigation


Demo wait for element hidden and visible
    &{options} =    create dictionary   headless=${False}
    Open browser    https://www.w3schools.com/js/js_ajax_intro.asp   options=${options}
    Run Async Keywords
    ...    Click Element    css:#demo button
    ...    AND    Wait for response url    https://www.w3schools.com/js/ajax_info.txt
    Wait Until Element Is Hidden    css:#demo button
    Wait Until Page Contains    AJAX is not a programming language    
    Wait Until Page Does Not Contains    Hello world
    
Demo wait for element contains text
    &{options} =    create dictionary   headless=${False}
    Open browser    https://www.w3schools.com/js/js_ajax_intro.asp   options=${options}
    Wait Until Element Contains    css:#demo h2    Let AJAX change this text
    
