*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Db And Go To Starting Page

*** Test Cases ***
Created book should be seen in view page
    [Tags]  view_book
    Click Link  Create a Book Reference
    Create a book reference  key=kirja123  author=kalle  title=kallen kirja  year=1999  publisher=SKS
    Go To Starting Page
    Click Link  View Book References
    Page Should Contain  Key: kirja123

Created article should be seen in view page
    [Tags]  view_article
    Click Link  Create an Article Reference
    Create an article reference  key=artikkeli123  author=kalle  title=kallen artikkeli  year=1998  journal=lehti
    Go To Starting Page
    Click Link  View Article References
    Page Should Contain  Key: artikkeli123

Created inproceedings should be seen in view page
    [Tags]  view_inproceedings
    Click Link  Create an Inproceedings Reference
    Create an inproceedings reference  key=inproceedings123  author=kalle  title=kallen inproceedings  year=1997  booktitle=kirja
    Go To Starting Page
    Click Link  View Inproceedings References
    Page Should Contain  Key: inproceedings123