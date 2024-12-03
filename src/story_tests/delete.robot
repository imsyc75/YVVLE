*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Db And Go To Starting Page

*** Test Cases ***
Deleted book is not in the database
    [Tags]  delete_book
    Click Link  Create a Book Reference
    Input Text  name=key  ABC
    Input Text  name=author  kalle
    Input Text  name=title  kallen kirja
    Input Text  name=year  1999
    Input Text  name=publisher  SKS
    # Create Book  ABC  kalle  kallen kirja  1999  SKS
    Click Button  Create
    Go To Starting Page
    Click Link  Delete References
    Select Checkbox  ABC
    Click Button  Delete
    ${books}=  Get Books
    Should Be Equal  ${books}  ${EMPTY}
