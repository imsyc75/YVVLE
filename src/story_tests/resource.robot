*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.5 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${BROWSER}    chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Reset Db
    Go To  ${RESET_URL}

Go To Starting Page
    Go To  ${HOME_URL}

Starting Page Should Be Open
    Page Should Contain  Welcome to BibTex References

Reset Db And Go To Starting Page
    Reset Db
    Go To  ${HOME_URL}

Create a book reference
    [Arguments]  ${key}=  ${author}=  ${title}=  ${year}=  ${publisher}=
    Input Text  name=key  ${key}
    Input Text  name=author  ${author}
    Input Text  name=title  ${title}
    Input Text  name=year  ${year}
    Input Text  name=publisher  ${publisher}
    Click Button  Create

Create an article reference
    [Arguments]  ${key}=  ${author}=  ${title}=  ${year}=  ${journal}=
    Input Text  name=key  ${key}
    Input Text  name=author  ${author}
    Input Text  name=title  ${title}
    Input Text  name=year  ${year}
    Input Text  name=journal  ${journal}
    Click Button  Create

Create an inproceedings reference
    [Arguments]  ${key}=  ${author}=  ${title}=  ${year}=  ${booktitle}=
    Input Text  name=key  ${key}
    Input Text  name=author  ${author}
    Input Text  name=title  ${title}
    Input Text  name=year  ${year}
    Input Text  name=booktitle  ${booktitle}
    Click Button  Create
