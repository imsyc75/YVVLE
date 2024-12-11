*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Db And Go To Starting Page

*** Test Cases ***
Clicking book edit link opens edit page for book
    [Tags]  edit_book_link
    Click Link  Create a Book Reference
    Create a book reference  key=kirja123  author=kalle  title=kallen kirja  year=1999  publisher=SKS
    Go To Starting Page
    Click Link  View Book References
    Click Link  Edit Reference
    Page Should Contain  Edit Book reference
    
Clicking article edit link opens edit page for article
    [Tags]  edit_article_link
    Click Link  Create an Article Reference
    Create an article reference  key=artikkeli123  author=kalle  title=kallen artikkeli  year=1998  journal=lehti
    Go To Starting Page
    Click Link  View Article References
    Click Link  Edit Reference
    Page Should Contain  Edit Article Reference

Clicking inproceedings edit link opens edit page for inproceedings
    [Tags]  edit_inproceedings_link
    Click Link  Create an Inproceedings Reference
    Create an inproceedings reference  key=inproceedings123  author=kalle  title=kallen inproceedings  year=1997  booktitle=kirja
    Go To Starting Page
    Click Link  View Inproceedings References
    Click Link  Edit Reference
    Page Should Contain  Edit Inproceedings Reference

Editing book shows correctly when viewing
    [Tags]  edit_book_view
    Click Link  Create a Book Reference
    Create a book reference  key=kirja123  author=kalle  title=kallen kirja  year=1999  publisher=SKS
    Go To Starting Page
    Click Link  View Book References
    Click Link  Edit Reference
    Input Text  name=author  sami
    Click Button  Update Book
    Page Should Contain  Author: sami

Editing article shows correctly when viewing
    [Tags]  edit_article_view
    Click Link  Create an Article Reference
    Create an article reference  key=artikkeli123  author=kalle  title=kallen artikkeli  year=1999  journal=lehti
    Go To Starting Page
    Click Link  View Article References
    Click Link  Edit Reference
    Input Text  name=author  sami
    Click Button  Update Article
    Page Should Contain  Author: sami

Editing inproceedings shows correctly when viewing
    [Tags]  edit_inproceedings_view
    Click Link  Create an Inproceedings Reference
    Create an inproceedings reference  key=inproceedings123  author=kalle  title=kallen inproceedings  year=1999  booktitle=kirja
    Go To Starting Page
    Click Link  View Inproceedings References
    Click Link  Edit Reference
    Input Text  name=author  sami
    Click Button  Update Inproceedings
    Page Should Contain  Author: sami
