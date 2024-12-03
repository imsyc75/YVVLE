*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Db And Go To Starting Page

*** Test Cases ***
Clicking book create link opens the right page
    [Tags]  create_book_link
    Click Link  Create a Book Reference
    Create Page Should Be Open

Clicking article create link opens the right page
    [Tags]  create_article_link
    Click Link  Create an Article Reference
    Create Page Should Be Open

Clicking inproceedings create link opens the right page
    [Tags]  create_inproceedings_link
    Click Link  Create an Inproceedings Reference
    Create Page Should Be Open

Creating a book reference adds it to the database
    [Tags]  create_book
    Click Link  Create a Book Reference
    Create a book reference  key=kirja123  author=kalle  title=kallen kirja  year=1999  publisher=SKS
    ${book}=  Get Books
    Should Be Equal  ${book}  kirja123 kalle kallen kirja 1999 SKS

Creating an article reference adds it to the database
    [Tags]  create_article
    Click Link  Create an Article Reference
    Create an article reference  key=artikkeli123  author=kalle  title=kallen artikkeli  year=1998  journal=lehti
    ${article}=  Get Articles
    Should Be Equal  ${article}  artikkeli123 kalle kallen artikkeli 1998 lehti

Creating an inproceedings reference adds it to the database
    [Tags]  create_inproceedings
    Click Link  Create an Inproceedings Reference
    Create an inproceedings reference  key=inproceedings123  author=kalle  title=kallen inproceedings  year=1997  booktitle=kirja
    ${inproceedings}=  Get Inproceedings
    Should Be Equal  ${inproceedings}  inproceedings123 kalle kallen inproceedings 1997 kirja

*** Keywords ***
Create Page Should Be Open
    Title Should Be  Create a new Reference