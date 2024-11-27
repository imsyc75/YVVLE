*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Db And Go To Starting Page

*** Test Cases ***
Created book should be seen in view page
    [Tags]  view_book
    Click Link  Create a Book Reference
    Input Text  name=key  ABC
    Input Text  name=author  kalle
    Input Text  name=title  kallen kirja
    Input Text  name=year  1999
    Input Text  name=publisher  SKS
    Click Button  Create
    Go To Starting Page
    Click Link  View Book References
    Page Should Contain  Key: ABC

Created article should be seen in view page
    [Tags]  view_article
    Click Link  Create an Article Reference
    Input Text  name=key  ABC
    Input Text  name=author  kalle
    Input Text  name=title  kallen artikkeli
    Input Text  name=year  1998
    Input Text  name=journal  lehti
    Click Button  Create
    Go To Starting Page
    Click Link  View Article References
    Page Should Contain  Key: ABC

Created inproceedings should be seen in view page
    [Tags]  view_inproceedings
    Click Link  Create an Inproceedings Reference
    Input Text  name=key  ABC
    Input Text  name=author  kalle
    Input Text  name=title  kallen inproceedings
    Input Text  name=year  1997
    Input Text  name=booktitle  kirja
    Click Button  Create
    Go To Starting Page
    Click Link  View Inproceedings References
    Page Should Contain  Key: ABC