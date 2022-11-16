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
    Submit Register Credentials
    Register Should Succeed

Login After Successful Registration
    Set Username  moderator
    Set Password  secret123
    Set Password Confirmation  secret123
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page And Check It Is Open
    Set Username  moderator
    Set Password  secret123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  fi
    Set Password  secret123
    Set Password Confirmation  secret123
    Submit Register Credentials
    Register Should Fail With Message  Username is too short
    Go To Login Page And Check It Is Open
    Set Username  fi
    Set Password  secret123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

Register With Too Short Username And Valid Password
    Set Username  us
    Set Password  secret123
    Set Password Confirmation  secret123
    Submit Register Credentials
    Register Should Fail With Message  Username is too short

Register With Too Valid Username And Too Short Password
    Set Username  user
    Set Password  pass
    Set Password Confirmation  pass
    Submit Register Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  user
    Set Password  password1
    Set Password Confirmation  password2
    Submit Register Credentials
    Register Should Fail With Message  Password and password confirmation do not match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Go To Register Page And Check It Is Open
    Go To Register Page
    Register Page Should Be Open

Go To Login Page And Check It Is Open
    Go To Login Page
    Login Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
