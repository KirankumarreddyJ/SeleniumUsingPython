# Import nesessory libreries
from FunctionLibrery.globalFunctionLibrery import GlobalFunction
from FunctionLibrery.globalVariables import GlobalVariables as globVal
from FunctionLibrery.htmlFunctionLibrery import Report
import time

def TC_MC_001_LoginVerification():
    try:
        # ******************************************************
        reportStep = '';  waitTime = ''
        exitTestOnStepFail = True; dontExitTestOnStepFail = False
        passed = 'passed'; failed = 'failed'

        globVal.testCaseName = 'TC_MC_001_LoginVerification'
        globVal.testType = 'Regression'
        globVal.testBrowserName = 'Chrome'

        # Creating object to global function
        GF_Obj = GlobalFunction()
        # *********************************************************

        # Step 1
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Open the browser and Navigate to Application'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        globVal.testURL = GF_Obj.getDataFromDataSheet(globVal.testData_ExcelPath, globVal.testData_URLs_SheetName,
                                                      'Mercury Tours', 'ApplicationURL', passed, failed, reportStep,
                                                      exitTestOnStepFail, 1)
        GF_Obj.launchApplication(globVal.testBrowserName, globVal.testURL, waitTime)

        # Step 2
        # ===================================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Login with valid credentials'
        Report.customReportStepNum(globVal.stepNumber,globVal.stepName)
        # ====================================================================
        stepData = GF_Obj.getDataFromDataSheet(globVal.testData_ExcelPath,globVal.testData_Credentials_SheetName,
                                    globVal.testCaseName,'UserName',passed,failed,reportStep,exitTestOnStepFail,1)
        GF_Obj.setDataToWebObj('MC_UserName_TextBox',stepData,passed,failed,reportStep,waitTime,exitTestOnStepFail)
        stepData = GF_Obj.getDataFromDataSheet(globVal.testData_ExcelPath, globVal.testData_Credentials_SheetName,
                                    globVal.testCaseName, 'Password', passed, failed, reportStep, exitTestOnStepFail, 1)
        GF_Obj.setDataToWebObj('MC_Password_TextBox', stepData, passed, failed, reportStep, waitTime,
                               exitTestOnStepFail)

        GF_Obj.clickOnWebObj('MC_UserName_TextBox','',passed,failed,reportStep,waitTime,dontExitTestOnStepFail)
        GF_Obj.clickOnWebObj('MC_SignIn_Button','',passed,failed,reportStep,waitTime,exitTestOnStepFail)
        GF_Obj.clickOnWebObj('MC_SignIn_Button','',passed,failed,reportStep,waitTime,dontExitTestOnStepFail)
        GF_Obj.clickOnWebObj('MC_SignOff_Link','',passed,failed,reportStep,waitTime,exitTestOnStepFail)
        GF_Obj.clickOnWebObj('MC_SignOff_Link','',passed,failed,reportStep,waitTime,dontExitTestOnStepFail)

        # Step 3
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Logout from the application and close all the browsers'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        GF_Obj.closeAllBrowser(True)

    # Catch if Exception is occurred
    except Exception as e:
        pass

if __name__ == '__main__':
    TC_MC_001_LoginVerification()