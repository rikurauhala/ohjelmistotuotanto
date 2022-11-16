*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Check It Is Open

*** Test Cases ***
Register With Valid Username And Password
    Set Username  admin
    Set Password  secret123
    Set Password Confirmation  secret123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  us
    Set Password  secret123
    Set Password Confirmation  secret123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Too Valid Username And Too Short Password
    Set Username  user
    Set Password  pass
    Set Password Confirmation  pass
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  user
    Set Password  password1
    Set Password Confirmation  password2
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Go To Register Page And Check It Is Open
    Go To Register Page
    Register Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
