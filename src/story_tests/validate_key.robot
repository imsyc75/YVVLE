*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Db And Go To Starting Page

*** Test Cases ***
Book with the same key isnt inserted into db
    Click Link  Create a Book Reference
    Create Book  ABC  kalle  kallen kirja  1999  SKS
    Create Book  ABC  sami  samin kirja  1998  Karisto
    ${books}=  Get Books
    Should Be Equal  ${books}  ABC kalle kallen kirja 1999 SKS

Article with the same key isnt inserted into db
    Click Link  Create an Article Reference
    Create Article  ABC  kalle  kallen artikkeli  1999  lehti
    Create Article  ABC  sami  samin artikkeli  1998  lehti
    ${articles}=  Get Articles
    Should Be Equal  ${articles}  ABC kalle kallen artikkeli 1999 lehti

Inproceedings with the same key isnt inserted into db
    Click Link  Create an Inproceedings Reference
    Create Inproceedings  ABC  kalle  kallen inproceedings  1999  kirja
    Create Inproceedings  ABC  sami  samin inproceedings  1998  kirja
    ${inproceedings}=  Get Inproceedings
    Should Be Equal  ${Inproceedings}  ABC kalle kallen inproceedings 1999 kirja

