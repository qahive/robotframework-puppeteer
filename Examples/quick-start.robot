*** Settings ***
Library    PuppeteerLibrary
Test Teardown    Close Browser


*** Test Cases ***
Example login form submit
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272   options=${options}
    Maximize Browser Window
    Input text    id:username_field    demo
    Input text    id:password_field    mode
    Run Async Keywords
    ...    Click Element    id:login_button    AND
    ...    Wait For Response Url    http://127.0.0.1:7272/welcome.html
    Wait Until Page Contains    Login succeeded
    # Logout and wait for homepage loaded
    Run Async Keywords
    ...    Click Link    partial link:logout    AND
    ...    Wait For Response Url    http://127.0.0.1:7272/

Control browser example
    ${HEADLESS}     Get variable value    ${HEADLESS}    ${False}
    &{options} =    create dictionary   headless=${HEADLESS}
    Open browser    http://127.0.0.1:7272   options=${options}
    Maximize Browser Window
    Go to   https://www.google.com
    Go back
    Reload page
    ${header} =    Get Text    css:h1
    Should Be Equal    Login Page    ${header}

*** Keywords ***
Test Teardown
    Close browser
