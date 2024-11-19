*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Go To Starting Page

*** Test Cases ***
Click Create Link
    [Tags]  create
    Click Link  Create a new Reference
    Create Page Should Be Open

Create A New Reference