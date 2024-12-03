*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Db And Go To Starting Page

*** Test Cases ***
Click Delete Link
    [Tags]  delete_link
    Click Link  Delete References
    Delete Page Should Be Open

Deleted book is not in the database
    [Tags]  delete_book
    Click Link  Create a Book Reference
    Create a book reference  key=kirja123  author=kalle  title=kallen kirja  year=1999  publisher=SKS
    Go To Starting Page
    Click Link  Delete References
    Select Checkbox  kirja123
    Click Button  Delete
    Page Should Not Contain  kirja123
    ${books}=  Get Books
    Should Be Equal  ${books}  ${EMPTY}

Deleted article is not in the database
    [Tags]  delete_article
    Click Link  Create an Article Reference
    Create an article reference  key=artikkeli123  author=kalle  title=kallen artikkeli  year=1998  journal=lehti
    Go To Starting Page
    Click Link  Delete References
    Select Checkbox  artikkeli123
    Click Button  Delete
    Page Should Not Contain  artikkeli123
    ${articles}=  Get Articles
    Should Be Equal  ${articles}  ${EMPTY}

Deleted inproceedings is not in the database
    [Tags]  delete_inproceedings
    Click Link  Create an Inproceedings Reference
    Create an inproceedings reference  key=inproceedings123  author=kalle  title=kallen inproceedings  year=1997  booktitle=kirja
    Go To Starting Page
    Click Link  Delete References
    Select Checkbox  inproceedings123
    Click Button  Delete
    Page Should Not Contain  inproceedings123
    ${inproceedings}=  Get Inproceedings
    Should Be Equal  ${inproceedings}  ${EMPTY}

*** Keywords ***
Delete Page Should Be Open
    Title Should Be  Delete References
