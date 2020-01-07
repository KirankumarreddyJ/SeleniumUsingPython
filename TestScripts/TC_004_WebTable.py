from FunctionLibrery.globalFunctionLibrery import GlobalFunction
from FunctionLibrery.globalVariables import GlobalVariables as globVal
from FunctionLibrery.htmlFunctionLibrery import Report
import time

def TC_004_WebTable():
    try:
        reportStep = '';waitTime ='';
        exitTestOnStepFail = True; dontExitTestOnStepFail = False
        globVal.testCaseName = 'TC_004_WebTable'
        globVal.testType = 'Regression'
        globVal.testBrowser = 'chrome'
        globVal.testURL = 'https://chercher.tech/python/table-selenium-python#'

        # Creating object to global function
        GF_Obj = GlobalFunction()

        testData = GF_Obj.getDataFromDataSheet('',globVal.testData_TestData_SheetName,'TC_001_Login','UserName','passed','failed',reportStep,dontExitTestOnStepFail,3)
        # Step 1
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Open the browser and Navigate to ' + globVal.testURL
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        GF_Obj.launchApplication(globVal.testBrowser,globVal.testURL,waitTime)
        #GF_Obj.verifyWebObjDisplayed('SignUp_page', 'Passed', 'Failed', 'stepName', 'ExitTest', 'WaitTime')
        object = globVal.driver.find_element_by_id('webtable')
        globVal.stepDiscription = 'CherCherTech - WebTable'
        GF_Obj.verifyWebObjDisplayed(object, 'Passed', 'Failed', reportStep, waitTime, dontExitTestOnStepFail)
        GF_Obj.verifyWebObjDisplayed('CherCherTech_Table_WebElement', 'Passed', 'Failed', reportStep, waitTime, exitTestOnStepFail)

        GF_Obj.verifyWebObjEnabled('CherCherTech_JIRA_Link','passed','failed',reportStep,waitTime,dontExitTestOnStepFail)
        #GF_Obj.clickOnWebObj('CherCherTech_JIRA_Link','','passed','failed',reportStep,waitTime,dontExitTestOnStepFail)
        GF_Obj.clickOnWebObj('CherCherTech_JIRA_Link','CherCherTech_JIRA_Page','passed','failed',reportStep,waitTime,exitTestOnStepFail)
        globVal.driver.back()


        Result = GF_Obj.getRowCountOfWebTable('CherCherTech_Table_WebElement','passed','failed',reportStep,dontExitTestOnStepFail,waitTime)
        print('Total Rows', Result)
        Result = GF_Obj.getColumnCountOfWebTable('CherCherTech_Table_WebElement','passed','failed',reportStep,dontExitTestOnStepFail,waitTime)
        print('Total Columns', Result)
        Result = GF_Obj.getCellDataFromWebTable('CherCherTech_Table_WebElement',2,3,'passed','failed',reportStep,dontExitTestOnStepFail,waitTime)
        print('Cell value', Result)
        Result = GF_Obj.verifyWebTableCellExist('CherCherTech_Table_WebElement',2,3,'passed','failed',reportStep,waitTime,dontExitTestOnStepFail)
        print('Cell Present', Result)
        Result = GF_Obj.getCellDataFromWebTable('CherCherTech_Table_WebElement',2,3,'passed','failed',reportStep,dontExitTestOnStepFail,waitTime)
        print('Cell value', Result)
        Result = GF_Obj.getTotalDataOfWebTable('CherCherTech_Table_WebElement','passed','failed',reportStep,dontExitTestOnStepFail,waitTime)
        print('Total value', Result)
        Result = GF_Obj.verifyWebObjEnabled('CherCherTech_Link1_Link','passed','failed',reportStep,dontExitTestOnStepFail,waitTime)
        print('Is Enabled', Result)
        Result = GF_Obj.verifyWebObjDisplayed('CherCherTech_Link2_Link', 'passed', 'failed', reportStep, dontExitTestOnStepFail, waitTime)
        print('Is Displayed', Result)
        GF_Obj.closeAllBrowser(False)

        globVal.testURL = 'https://www.thetestingworld.com/testings/'
        # Step 2
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Open the browser and Navigate to ' + globVal.testURL
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        GF_Obj.launchApplication(globVal.testBrowser, globVal.testURL, waitTime)

        # Step 3
        # ====================================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Login to the application'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ===================================================================
        GF_Obj.clickOnWebObj('SignUp_Login_Link', '', 'Passed', 'Failed', 'Click on Login link in SignUp page',
                             waitTime,dontExitTestOnStepFail)
        testData = GF_Obj.getDataFromDataSheet('', globVal.testData_Credentials_SheetName, 'TestingWorld',
                                               'UserName', 'Passed', 'Failed', reportStep, dontExitTestOnStepFail,1)
        GF_Obj.setDataToWebObj('Login_UserID_TextBox', testData, 'Passed', 'Failed', 'Enter value into user id textbox',
                               waitTime,dontExitTestOnStepFail)
        testData = GF_Obj.getDataFromDataSheet('', globVal.testData_Credentials_SheetName, 'TestingWorld',
                                               'Password', 'Passed', 'Failed', reportStep,dontExitTestOnStepFail,1)
        GF_Obj.setDataToWebObj('Login_Password_TextBox', testData, 'Passed', 'Failed',
                               'Enter value into password textbox', waitTime,dontExitTestOnStepFail)
        GF_Obj.clickOnWebObj('Login_Login_Btn', '', 'Passed', 'Failed', 'Click on Login button', waitTime,dontExitTestOnStepFail)

        # Step 4
        # ==============================================================
        globVal.stepNumber = globVal.stepNumber + 1
        globVal.stepName = 'Select "Female" from sex dropdown in homepage'
        Report.customReportStepNum(globVal.stepNumber, globVal.stepName)
        # ==============================================================
        # GF_Obj.selectDropdownWebObjValByName('HomePage_Sex_Dropdown', 'Female', 'Passed', 'Failed', reportStep,
        #                                      waitTime, dontExitTestOnStepFail)
        GF_Obj.selectDropdownWebObjValByIndex('HomePage_Sex_Dropdown', 2, 'Passed', 'Failed', reportStep,
                                             waitTime, dontExitTestOnStepFail)
        GF_Obj.closeAllBrowser('Yes')
    # Catch if Exception is occurred
    except Exception as e:
        exceptionType = str(type(e).__name__)
        if exceptionType.lower() != 'exception':
            # Report Step as 'Failed'
            stepName = 'Exception occurred in test execution. (ExceptionType: &lt;' + exceptionType + '&gt;)'
            stepDetail = 'Description: &lt;'+str(e)+'&gt;'
            Report.customReport(stepName, stepDetail, 'Failed')
            # Save HTML Report
            GF_Obj.saveHTMLReport()
        else:
            pass

if __name__ == '__main__':
    TC_004_WebTable()