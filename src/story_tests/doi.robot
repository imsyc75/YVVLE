*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Db And Go To Starting Page

*** Variables ***
${false_doi}         https://doi.org/10.1145/367473
${real_doi}          https://doi.org/10.1145/3674735
${real_doi_author}   Thangamani, Arun and Loechner, Vincent and Genaud, Stéphane
${real_doi_title}    A Survey of General-purpose Polyhedral Compilers
${real_doi_year}     2024
${real_doi_journal}  ACM Transactions on Architecture and Code Optimization

*** Test Cases ***
Clicking upload doi reference opens the right page
    [Tags]  click_doi
    Click Link  Upload DOI reference
    Title Should Be  Upload DOI reference
    Page Should Contain  Here you can add DOI Reference
    Page Should Contain Textfield  doi

Inputting an empty doi gives an error message
    [Tags]  empty_doi
    Click Link  Upload DOI reference
    Click Button  Upload
    Page Should Contain  The doi link was given incorrectly

Inputting a doi which does not exist gives an error message
    [Tags]  doesntexist_doi
    Click Link  Upload DOI reference
    Input Text  name=doi  ${false_doi}
    Click Button  Upload
    Page Should Contain  Such a doi does not exist

Inputting a real doi redirects to doi edit page with filled fields
    [Tags]  real_doi_redirects
    Click Link  Upload DOI reference
    Input Text  name=doi  ${real_doi}
    Click Button  Upload
    Page Should Contain  Found article reference with fields:
    Textfield Value Should Be  name=author  ${real_doi_author}
    Textfield Value Should Be  name=title  ${real_doi_title}
    Textfield Value Should Be  name=year  ${real_doi_year}
    Textfield Value Should Be  name=journal  ${real_doi_journal}

Input doi can be viewed in view page
    [Tags]  view_doi
    Click Link  Upload DOI reference
    Input Text  name=doi  ${real_doi}
    Click Button  Upload
    Input Text  name=key  doi123
    Click Button  Add
    Go To Starting Page
    Click Link  View Article References
    Page Should Contain  Key: doi123

Editing doi before adding edits the reference correctly
    [Tags]  edit_doi
    Click Link  Upload DOI reference
    Input Text  name=doi  ${real_doi}
    Click Button  Upload
    Input Text  name=key  doi123
    Input Text  name=author  kalle
    Click Button  Add
    Go To Starting Page
    Click Link  View Article References
    Page Should Contain  Key: doi123
    Page Should Contain  Author: kalle
    Page Should Not Contain  Author: ${real_doi_author}