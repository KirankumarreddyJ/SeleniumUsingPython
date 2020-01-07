from FunctionLibrery.globalFunctionLibrery import GlobalFunction
from FunctionLibrery.globalVariables import GlobalVariables as globVal
from FunctionLibrery.htmlFunctionLibrery import Report

def TC_001_Login():
    try:
        reportStep = ''; waitTime = ''; exitTestOnStepFail = True; dontExitTestOnStepFail = False
        passed = 'passed'; failed = 'failed'
        globVal.testCaseName = 'TC_001_Login'
        globVal.testType = 'Regression'

        #Creating object to global function
        GF_Obj = GlobalFunction()

    #Step 1
    # ==============================================================
        globVal.stepNumber = globVal.stepNumber+1
        globVal.stepName = 'Open the browser and Navigate to Testing World Signup page'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
    # ==============================================================
        globVal.testURL = GF_Obj.getDataFromDataSheet(globVal.testData_ExcelPath, 'URLs', 'TestingWorld','ApplicationURL',
                                                      'information', 'warning', reportStep, exitTestOnStepFail, 1)
        GF_Obj.launchApplication('Chrome',globVal.testURL,20)
        GF_Obj.verifyNavigation('SignUpPage',passed,failed,reportStep,waitTime,dontExitTestOnStepFail)

    # Step 2
    # ====================================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Login to the application'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
    # ===================================================================
        GF_Obj.clickOnWebObj('SignUp_Login_Link', 'LoginPage', passed,failed,reportStep,waitTime,exitTestOnStepFail)
        GF_Obj.clickOnWebObj('SignUp_Login_L ink', 'LoginPage', passed,failed,reportStep,waitTime,dontExitTestOnStepFail)

        testData = GF_Obj.getDataFromDataSheet(globVal.testData_ExcelPath,globVal.testData_Credentials_SheetName,
                                               'TestingWorld','UserName',passed,failed,reportStep,exitTestOnStepFail,1)
        GF_Obj.setDataToWebObj('Login_UserID_TextBox', testData, passed, failed, reportStep, waitTime, exitTestOnStepFail)
        testData = GF_Obj.getDataFromDataSheet(globVal.testData_ExcelPath, globVal.testData_Credentials_SheetName,
                                               'TestingWorld', 'Password', passed, failed, reportStep, exitTestOnStepFail,1)
        GF_Obj.setDataToWebObj('Login_Password_TextBox', testData, passed,failed,reportStep,waitTime,exitTestOnStepFail)
        GF_Obj.clickOnWebObj('Login_Logi n_Btn', 'HomePage', passed,failed,reportStep,waitTime,dontExitTestOnStepFail)
        GF_Obj.clickOnWebObj('Login_Login_Btn', 'HomePage', passed,failed,reportStep,waitTime,exitTestOnStepFail)

        # ---------------
        # globVal.driver.switch_to_frame(0)
        # GF_Obj.setDataToWebObj('HomePage_ViewLarge_ChooseFile','C://Users/Dell/Desktop/5b2e72383d53d.png',passed,failed,reportStep,waitTime,dontExitTestOnStepFail)
        # GF_Obj.clickOnWebObj('HomePage_ViewLarge_Upload','',passed,failed,reportStep,waitTime,dontExitTestOnStepFail)
        filePath = 'C://Users/Dell/Desktop/5b2e72383d53d.png'
        GF_Obj.uploadFile('HomePage_ViewLarge_ChooseFile','HomePage_ViewLarge_Upload',filePath,passed,failed,reportStep,waitTime,dontExitTestOnStepFail)
        # ---------------

    # Step 3
    # ==============================================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Logout from the application and close all the browsers'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
    # ===============================================================================
        GF_Obj.clickOnWebObj('HomePage_Logout_Btn', 'SignUpPage', passed,failed,reportStep,waitTime,exitTestOnStepFail)
        GF_Obj.closeAllBrowser('Yes')

    # Catch if Exception is occurred
    except Exception as e:
        exceptionType = str(type(e).__name__)
        if exceptionType.lower() != 'exception':
            # Report Step as 'Failed'
            stepName = 'Exception occurred in test execution. (ExceptionType: &lt;' + exceptionType + '&gt;)'
            stepDetail = 'Description: &lt;' + str(e) + '&gt;'
            Report.customReport(stepName, stepDetail, 'Failed')
            # Save HTML Report
            GF_Obj.saveHTMLReport()
        else:
            pass

if __name__ == '__main__':
    TC_001_Login()