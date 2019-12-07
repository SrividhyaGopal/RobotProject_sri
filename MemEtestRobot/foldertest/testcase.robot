*** Settings ***
Library    SeleniumLibrary
Test Setup        Log    In test set up    
Test Teardown     Log    In test tear down   
Suite Setup    Log    In test suite    
Suite Teardown    Log    In suite tear down     
Default Tags    sanity
*** Test Cases ***
Mysectest
    Log    very easy 
    
FirstSeleniumTest
  
   Open Browser    https://google.com    firefox
    Set Browser Implicit Wait    5
   Input Text    name=q    TestPython
   Press Keys    name=q    ENTER
   # Click Button    class=gNO89b    
   Sleep    3           
   Close Browser 
   Log    Test completed    
    

SampleLoginTest
    [Documentation]    This a sample login test
    Open Browser        ${url}     chrome  
    Set Browser Implicit Wait    15
    LoginKW
    Click Element      id=welcome   
    Close Browser 
    # Click Element      link=Logout  
    Log    Test complete  
    Log    This test was executed by %{username} in %{os}     
    
*** Variables ***
${url}    https://opensource-demo.orangehrmlive.com  
@{credentials}    Admin    admin123  
&{LoginData}    Username=Admin    Password=admin123

*** Keywords ***
LoginKW
    Input Text         id=txtUsername    @{credentials}[0]
    Input Password     id=txtPassword    &{LoginData}[Password] 
    Click Button       id=btnLogin  
    
    
            
    
    
        
    ...     
    
    

    