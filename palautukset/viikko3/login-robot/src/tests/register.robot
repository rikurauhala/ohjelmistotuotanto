*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  user  password123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  admin  password321
    Output Should Contain  User with username admin already exists

Register With Too Short Username And Valid Password
    Input Credentials  us  password123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  user  pass
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  user  password
    Output Should Contain  Password is invalid

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  admin  secret123
    
