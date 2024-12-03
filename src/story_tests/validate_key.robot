*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Db And Go To Starting Page

*** Test Cases ***
Book with the same key isnt inserted into db
    Click Link  Create a Book Reference
    Create a book reference  key=kirja123  author=kalle  title=kallen kirja  year=1999  publisher=SKS
    Click Link  Create a Book Reference
    Create a book reference  key=kirja123  author=sami  title=samin kirja  year=1998  publisher=Karisto
    ${books}=  Get Books
    Should Be Equal  ${books}  kirja123 kalle kallen kirja 1999 SKS

Article with the same key isnt inserted into db
    Click Link  Create an Article Reference
    Create an article reference  key=artikkeli123  author=kalle  title=kallen artikkeli  year=1999  journal=lehti
    Click Link  Create an Article Reference
    Create an article reference  key=artikkeli123  author=sami  title=samin artikkeli  year=1998  journal=toinen lehti
    ${articles}=  Get Articles
    Should Be Equal  ${articles}  artikkeli123 kalle kallen artikkeli 1999 lehti

Inproceedings with the same key isnt inserted into db
    Click Link  Create an Inproceedings Reference
    Create an inproceedings reference  key=inproceedings123  author=kalle  title=kallen inproceedings  year=1999  booktitle=kirja
    Click Link  Create an Inproceedings Reference
    Create an inproceedings reference  key=inproceedings123  author=sami  title=samin inproceedings  year=1997  booktitle=toinen kirja
    ${inproceedings}=  Get Inproceedings
    Should Be Equal  ${Inproceedings}  inproceedings123 kalle kallen inproceedings 1999 kirja

