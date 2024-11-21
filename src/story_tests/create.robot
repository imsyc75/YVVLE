*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Go To Starting Page

*** Test Cases ***
Click Create Link
    [Tags]  create
    Click Link  Create a Book Reference
    Create Page Should Be Open

Create Reference
    [Tags]  create2
    Click Link  Create a Book Reference
    Create Book  asd  kalle  kallen kirja  SKS  1999
    Click Button  Create
    ${book}=  Get Books
    Should Be Equal  ${book}  asd kalle kallen kirja SKS 1999