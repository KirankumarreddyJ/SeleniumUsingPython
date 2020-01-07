from FunctionLibrery.globalFunctionLibrery import GlobalFunction
from FunctionLibrery.globalVariables import GlobalVariables as globVal
from FunctionLibrery.htmlFunctionLibrery import Report
import time

def TC_005_WindowHandles():
    try:
        ###########################################################
        reportStep = ''; waitTime = '';
        exitTestOnStepFail = True;  dontExitTestOnStepFail = False
        passed = 'passed';  failed = 'failed'
        globVal.testCaseName = 'TC_005_WindowHandles'
        globVal.testType = 'Regression'
        globVal.testBrowserName = 'Chrome'

        # Creating object to global function
        GF_Obj = GlobalFunction()
        ############################################################

        # Step 1
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Open the browser and Navigate to Application'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        #globVal.testURL = 'https://www.thetestingworld.com/testings/'
        globVal.testURL = GF_Obj.getDataFromDataSheet(globVal.testData_ExcelPath,globVal.testData_URLs_SheetName,'TestingWorld','ApplicationURL',passed,failed,reportStep,exitTestOnStepFail,1)
        GF_Obj.launchApplication('ie', globVal.testURL, waitTime)

        # Step 2
        # ====================================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Login to the application'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ===================================================================
        GF_Obj.clickOnWebObj('SignUp_Login_Link', '', 'Passed', 'Failed', 'Click on Login link in SignUp page',
                             waitTime, exitTestOnStepFail)
        testData = GF_Obj.getDataFromDataSheet('', globVal.testData_Credentials_SheetName, 'TestingWorld',
                                               'UserName', 'Passed', 'Failed', reportStep, exitTestOnStepFail, 1)
        GF_Obj.setDataToWebObj('Login_UserID_TextBox', testData, 'Passed', 'Failed', 'Enter value into user id textbox',
                               waitTime, dontExitTestOnStepFail)
        testData = GF_Obj.getDataFromDataSheet('', globVal.testData_Credentials_SheetName, 'TestingWorld',
                                               'Password', 'Passed', 'Failed', reportStep, dontExitTestOnStepFail, 1)
        GF_Obj.setDataToWebObj('Login_Password_TextBox', testData, 'Passed', 'Failed',
                               'Enter value into password textbox', waitTime, dontExitTestOnStepFail)
        GF_Obj.clickOnWebObj('Login_Login_Btn', '', 'Passed', 'Failed', 'Click on Login button', waitTime,
                             dontExitTestOnStepFail)

        # Step 4
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Select "Female" from sex dropdown in homepage'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================

        GF_Obj.switchToSimpleAlert(True, True, passed, failed, reportStep, waitTime, dontExitTestOnStepFail)
        GF_Obj.switchToSimpleAlert(True, False, passed, failed, reportStep, waitTime, dontExitTestOnStepFail)
        GF_Obj.switchToSimpleAlert(False, True, passed, failed, reportStep, waitTime, dontExitTestOnStepFail)
        GF_Obj.switchToSimpleAlert(False, False, passed, failed, reportStep, waitTime, dontExitTestOnStepFail)
        GF_Obj.switchToSimpleAlert(True, True, passed, failed, reportStep, waitTime, dontExitTestOnStepFail)

        GF_Obj.clickOnWebObj('HomePage_TestingProdSite_Link', '', passed, failed, reportStep, waitTime,dontExitTestOnStepFail)

        print('window size: ', globVal.driver.get_window_size())
        print('current window: ', globVal.driver.current_window_handle)
        obj1 = globVal.driver.window_handles[0]

        print('window 1', globVal.driver.title)

        obj2 = globVal.driver.window_handles[1]
        globVal.driver.switch_to.window(obj2)
        print('window 2', globVal.driver.title)
        globVal.driver.switch_to.window(obj1)
        print('window 1', globVal.driver.title)

        GF_Obj.switchWindowByIndex('1', passed, failed, reportStep, dontExitTestOnStepFail)
        print('window 2 function', globVal.driver.title)
        GF_Obj.switchWindowByIndex(' 0', passed, failed, reportStep, dontExitTestOnStepFail)
        print('window 1 function', globVal.driver.title)
        GF_Obj.switchWindowByIndex(3, passed, failed, reportStep, exitTestOnStepFail)
        print('window 3 function', globVal.driver.title)
        GF_Obj.switchWindowByIndex(4, passed, failed, reportStep, dontExitTestOnStepFail)
        print('window 4 function', globVal.driver.title)
        GF_Obj.switchWindowByIndex('jk', passed, failed, reportStep, dontExitTestOnStepFail)
        print('window 1 function', globVal.driver.title)
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
    TC_005_WindowHandles()