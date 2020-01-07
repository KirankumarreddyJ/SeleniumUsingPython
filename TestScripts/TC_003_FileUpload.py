from FunctionLibrery.globalFunctionLibrery import GlobalFunction
from FunctionLibrery.globalVariables import GlobalVariables as globVal
from FunctionLibrery.htmlFunctionLibrery import Report
import time

def TC_003_FileUpload():
    try:
        globVal.testCaseName = 'TC_003_FileUpload'
        globVal.testType = 'Regression'

        #Creating object to global function
        GF_Obj = GlobalFunction()

        # Step 1
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Open the browser and Navigate to ' + globVal.testURL
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        GF_Obj.launchApplication()
        GF_Obj.verifyWebObjDisplayed('SignUp_page', 'Passed', 'Failed', 'StepName', 'ExitTest', 'WaitTime')

        # Step 2
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Login to the application'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        GF_Obj.clickOnWebObj('SignUp_Login_Link', 'LoginPage', 'Passed', 'Failed', 'Click on Login link in SignUp page',
                           'ExitTest', 'WaitTime')
        testData = GF_Obj.getDataFromDataSheet('filepath', globVal.testData_Credentials_SheetName, 'TestingWorld',
                                               'UserName', 'Passed', 'Failed', 'StepName', 'ExitTest')
        GF_Obj.setDataToWebObj('Login_UserID_TextBox', testData, 'Passed', 'Failed', 'Enter value into user id textbox',
                           'ExitTest', 'WaitTime')
        testData = GF_Obj.getDataFromDataSheet('filepath', globVal.testData_Credentials_SheetName, 'TestingWorld',
                                               'Password', 'Passed', 'Failed', 'StepName', 'ExitTest')
        GF_Obj.setDataToWebObj('Login_Password_TextBox', testData, 'Passed', 'Failed', 'Enter value into password textbox',
                           'ExitTest', 'WaitTime')
        GF_Obj.clickOnWebObj('Login_Login_Btn', 'HomePage', 'Passed', 'Failed', 'Click on Login button', 'ExitTest',
                           'WaitTime')

        # Step 3
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Select "" from sex dropdown in homepage'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        #GF_Obj.setValToObj('HomePage_ViewLarge_ChooseFile', '‪C:/Users/Dell/Desktop/Sample.png', 'Passed', 'Failed', 'Enter value into user id textbox',
                          # 'ExitTest', 'WaitTime')

        GF_Obj.clickOnWebObj('HomePage_ViewLarge_ChooseFile', '', 'Passed', 'Failed', 'Click on "Choose File" button under View Large Section  in Home page',
                           'ExitTest', 'WaitTime')
        time.sleep(3)

        GF_Obj.closeAllBrowser('Yes')
    except Exception as e:
        pass

if __name__ == '__main__':
    TC_003_FileUpload()