from FunctionLibrery.globalFunctionLibrery import GlobalFunction
from FunctionLibrery.globalVariables import GlobalVariables as globVal
from FunctionLibrery.htmlFunctionLibrery import Report

def TC_002_Signup():
    try:
        globVal.testCaseName = 'TC_002_Signup'
        globVal.testType = 'Regression'

        #Creating object to global function
        GF_Obj = GlobalFunction()

    #Step 1
    # ==============================================================
        globVal.stepNumber = globVal.stepNumber+1
        globVal.stepName = 'Open the browser and Navigate to '+ globVal.testURL
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
    # ==============================================================
        GF_Obj.launchApplication()
        GF_Obj.verifyWebObjDisplayed('SignUp_page', 'Passed', 'Failed', 'StepName', 'ExitTest', 'WaitTime')

    # Step 2
    # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Signup with valid details'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
    # ==============================================================
        testData = GF_Obj.getDataFromDataSheet('filepath', globVal.testData_TestData_SheetName, globVal.testCaseName,'UserName', 'Passed', 'Failed', 'StepName', 'ExitTest')
        GF_Obj.setDataToWebObj('SignUp_UserName_TextBox', testData, 'Passed', 'Failed', 'Enter User name into textbox', 'ExitTest', 'WaitTime')
        testData = GF_Obj.getDataFromDataSheet('filepath', globVal.testData_TestData_SheetName, globVal.testCaseName,'EmailId', 'Passed', 'Failed', 'StepName', 'ExitTest')
        GF_Obj.setDataToWebObj('SignUp_MailId_TextBox', testData, 'Passed', 'Failed', 'Enter Maild id into textbox', 'ExitTest', 'WaitTime')
        testData = GF_Obj.getDataFromDataSheet('filepath', globVal.testData_Credentials_SheetName, 'TestingWorld','Password', 'Passed', 'Failed', 'StepName', 'ExitTest')
        GF_Obj.setDataToWebObj('SignUp_Password_TextBox', testData, 'Passed', 'Failed', 'Enter password into textbox', 'ExitTest', 'WaitTime')
        GF_Obj.setDataToWebObj('SignUp_CnfPassword_TextBox', testData, 'Passed', 'Failed', 'Enter confirm password into textbox', 'ExitTest', 'WaitTime')
        testData = GF_Obj.getDataFromDataSheet('filepath', globVal.testData_TestData_SheetName, globVal.testCaseName,'DateOfBirth', 'Passed', 'Failed', 'StepName', 'ExitTest')
        GF_Obj.setDataToWebObj('SignUp_DateOfBirth_TextBox', testData, 'Passed', 'Failed', 'Enter Date of birth into textbox', 'ExitTest', 'WaitTime')
        testData = GF_Obj.getDataFromDataSheet('filepath', globVal.testData_TestData_SheetName, globVal.testCaseName,'PhoneNumber', 'Passed', 'Failed', 'StepName', 'ExitTest')
        GF_Obj.setDataToWebObj('SignUp_PhoneNumber_TextBox', testData, 'Passed', 'Failed', 'Enter Phone Number into textbox', 'ExitTest', 'WaitTime')
        testData = GF_Obj.getDataFromDataSheet('filepath', globVal.testData_TestData_SheetName, globVal.testCaseName,'Address', 'Passed', 'Failed', 'StepName', 'ExitTest')
        GF_Obj.setDataToWebObj('SignUp_Address_TextBox', testData, 'Passed', 'Failed', 'Enter Address into textbox', 'ExitTest', 'WaitTime')
        testData = GF_Obj.getDataFromDataSheet('filepath', globVal.testData_TestData_SheetName, globVal.testCaseName,'AddressType', 'Passed', 'Failed', 'StepName', 'ExitTest')
        if str(testData).lower() == 'home':
            obj = 'SignUp_Home_RadioBtn'
        elif str(testData).lower() == 'office':
            obj = 'SignUp_Office_RadioBtn'
        else:
            obj = None
            Report.customReport('Select address type', 'Entered address type in "TestData.xlsx" is invalid', 'Failed')
            GF_Obj.stopExecution()
        GF_Obj.clickOnWebObj(obj, '', 'Passed', 'Failed', 'Select Address type in SignUp page', 'ExitTest', 'WaitTime')
        GF_Obj.selectDropdownWebObjValByName('SignUp_Gender_DropDown', 'Male', 'Passed', 'Failed', 'Select Gender from dropdown', 'ExitTest', 'WaitTime')
        GF_Obj.selectDropdownWebObjValByName('SignUp_Country_DropDown', 'India', 'Passed', 'Failed', 'Select Country from dropdown', 'ExitTest', 'WaitTime')
        GF_Obj.selectDropdownWebObjValByName('SignUp_State_DropDown', 'Andhra Pradesh', 'Passed', 'Failed', 'Select State from dropdown', 'ExitTest', 'WaitTime')
        GF_Obj.selectDropdownWebObjValByName('SignUp_City_DropDown', 'Anantapur', 'Passed', 'Failed', 'Select City from dropdown', 'ExitTest', 'WaitTime')
        testData = GF_Obj.getDataFromDataSheet('filepath', globVal.testData_TestData_SheetName, globVal.testCaseName,'Zipcode', 'Passed', 'Failed', 'StepName', 'ExitTest')
        GF_Obj.setDataToWebObj('SignUp_ZipCode_TextBox', testData, 'Passed', 'Failed', 'Enter Zipcode into textbox', 'ExitTest', 'WaitTime')
        GF_Obj.clickOnWebObj('SignUp_Terms_CheckBox', '', 'Passed', 'Failed', 'StepName', 'ExitTest', 'WaitTime')

        GF_Obj.clickOnWebObj('SignUp_SignUp_Btn', '', 'Passed', 'Failed', 'StepName', 'ExitTest', 'WaitTime')
        # GF_Obj.verifyWebObj('HomePage_Logout_Btn','Passed','Failed','Verify Home page is displayed','ExitTest','WaitTime')
        try:
            message = globVal.driver.find_element_by_xpath('//div[@id="tab-content1"]/div').text
            if 'User is successfully Register. Now You can Login' in message:
                Report.customReport('Verify user successfully signed up', 'User successfully signed up', 'Passed')
            else:
                Report.customReport('Verify user successfully signed up', 'User is not successfully signed up Error is : "' + str(message) + '"', 'Failed')
        except Exception as error:
            Report.customReport('Verify user successfully signed up', 'User is not successfully signed up. Error is : "' + str(error) + '"', 'Failed')

        # Step 3
    # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Close all the browsers'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
    # ==============================================================
        GF_Obj.closeAllBrowser('Yes')
    except Exception as e:
        pass
if __name__ == '__main__':
    TC_002_Signup()