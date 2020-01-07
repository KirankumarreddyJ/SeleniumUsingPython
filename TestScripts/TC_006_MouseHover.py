from FunctionLibrery.globalFunctionLibrery import GlobalFunction
from FunctionLibrery.globalVariables import GlobalVariables as globVal
from FunctionLibrery.htmlFunctionLibrery import Report
import time

def TC_006_MouseHover():
    try:
        reportStep = ''; waitTime = ''; exitTestOnStepFail = True; dontExitTestOnStepFail = False
        passed = 'passed'; failed = 'failed'
        globVal.testCaseName = 'TC_006_MouseHover'
        globVal.testType = 'Regression'
        #globVal.testBrowser = 'chrome'
        globVal.testURL = 'https://facebook.com'

        # Creating object to global function
        GF_Obj = GlobalFunction()
        globVal.testURL = GF_Obj.getDataFromDataSheet(globVal.testData_ExcelPath,'URLs','TestingWorld','ApplicationURL','information','warning',reportStep,exitTestOnStepFail,1)
        # Step 1
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Open the browser and Navigate to ' + globVal.testURL
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        GF_Obj.launchApplication('Chrome', globVal.testURL, waitTime)

        # Step 2
        # ====================================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Login to the application'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ===================================================================
        GF_Obj.clickOnWebObj('SignUp_Login_Link', '', 'Passed', 'Failed', 'Click on Login link in SignUp page',
                             waitTime, dontExitTestOnStepFail)
        testData = GF_Obj.getDataFromDataSheet('', globVal.testData_Credentials_SheetName, 'TestingWorld',
                                               'UserName', 'Passed', 'Failed', reportStep, dontExitTestOnStepFail, 1)
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
        globVal.stepName = 'Hover the mouse on Hover button and click on Manage Customer link'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        globVal.driver.find_element_by_xpath('//input[@id="file" and @name="file"]').send_keys('‪C:\\Users\\Dell\\Desktop\\5b2e72383d53d.png')
        globVal.driver.find_element_by_id('//input[@type="submit" and @value="Upload"]').click()

        Object = globVal.driver.find_element_by_xpath('//a[text()="Hover "]')
        globVal.stepDiscription = 'Homepage Header - Hover Button'
        GF_Obj.mouseHoverOnWebObj('HomePage_Hover_Link',passed,failed,reportStep,waitTime,dontExitTestOnStepFail)
        time.sleep(5)
        Object = globVal.driver.find_element_by_xpath('(//a[text()="Manage Customer"])[2]')
        globVal.stepDiscription = 'Homepage Header - Manage Customer Link'
        GF_Obj.clickOnWebObj('HomePage_ManageCustomer_Link','',passed,failed,reportStep,waitTime,dontExitTestOnStepFail)
        time.sleep(5)

        GF_Obj.saveHTMLReport()
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
    TC_006_MouseHover()