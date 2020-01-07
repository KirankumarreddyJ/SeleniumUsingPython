from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Ie
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from FunctionLibrery.htmlFunctionLibrery import Report
from FunctionLibrery.globalVariables import GlobalVariables as globVal
from FunctionLibrery.constantLibrery import ConstantLibrery as cnsLib
import sys,openpyxl


class GlobalFunction:
    global WaitTime
    WaitTime=20
    def __init__(self):
        Report()
        #globVal.testURL = GlobalFunction.getDataFromDataSheet('filepath', globVal.testData_URLs_SheetName, 'TestingWorld', 'ApplicationURL','Information', 'Failed', 'StepName', 'ExitTest')
        #globVal.testURL = readConfigData.readTestData("BasicData", "Application_URL")
        #print("This is Global function constructor")

    # ------------------------ Common Functions ------------------------------------

    # ************************************************************************************
    # Function Name : getDriverForWebObj
    # Purpose       : To get the webdriver object for given webObject
    # Input         : Object Name (should be present in constant library under 'getObjLocator' function)
    # Returned Type : Webdriver Object or False(bool)
    # *************************************************************************************
    @staticmethod
    def getDriverObjForWebObj(webObject,waitTime):
        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            # set defailt waitTime 20
            waitTime = 20

        try:
            #locater = readConfigData.readLocatersData("Locaters", Object)
            locater = cnsLib.getObjLocator(webObject)
            locaterValList = locater.split(":", 1)
            locaterType = locaterValList[0].lower()
            locaterVal = locaterValList[1]
            driver = globVal.driver
            driver.implicitly_wait(waitTime)
            if locaterType == 'id':
                return driver.find_element_by_id(locaterVal)
            elif locaterType == 'xpath':
                return driver.find_element_by_xpath(locaterVal)
            elif locaterType == 'name':
                return driver.find_element_by_name(locaterVal)
            elif locaterType == 'classname':
                return driver.find_element_by_class_name(locaterVal)
            elif locaterType == 'cssselector':
                return driver.find_element_by_css_selector(locaterVal)
            elif locaterType == 'linktext':
                return driver.find_element_by_link_text(locaterVal)
            elif locaterType == 'partiallinktext':
                return driver.find_element_by_partial_link_text(locaterVal)
            elif locaterType == 'tagname':
                return driver.find_element_by_tag_name(locaterVal)
            else:
                #ReportStep = "Entered locator type('"+locaterType+"') in '"+locater+"' is not correct for &lt;" + str(Object)+ "&gt; Object"
                #Reports.customReport("Get Locator from ConstantLibrery", ReportStep, "Failed")
                #ReportStep = "Info: Locator Type should be any one of these: id, name, xpath, classname, cssselector, linktext, partiallinktext, tagname"
                #Reports.customReport(ReportStep,"" ,"Information")
                #GlobalFunction.stopExecution()
                return False
        # Catch if exception occurred
        except Exception as e:
            # Update Exception type to global variable
            GlobalFunction.setExceptionType(e)
            return False
    # ------------------------------------------------------------------------------------------------------------------

    # @staticmethod
    # def getTestData(Object):
    #     return readConfigData.readTestData("BasicData", Object)

    # ************************************************************************************
    # Function Name : stopExecution
    # Purpose       : To stop the execution instantly
    # Input         : NA
    # Returned Type : NA
    # *************************************************************************************
    @staticmethod
    def stopExecution():
        try:
            globVal.driver.quit()
        except Exception as e:
            Report.customReport("Close the browser", "Browser is not closed", "Failed")
        finally:
            Report.saveHTMLReport()
            # sys.exit(1)
            raise Exception('Exception occurred')
    # ------------------------------------------------------------------------------------------------------------------
    # ************************************************************************************
    # Function Name : saveHTMLReport
    # Purpose       : To save HTML report
    # Input         : NA
    # Returned Type : NA
    # *************************************************************************************
    @ staticmethod
    def saveHTMLReport():
        try:
            Report.saveHTMLReport()
        except Exception as e:
            exceptionType = str(type(e).__name__)
            print('html report is not saved. Exception Type:"'+exceptionType+'"')
    # ------------------------------------------------------------------------------------------------------------------
    # ************************************************************************************
    # Function Name : exitTest
    # Purpose       : To stop the execution if 'stopTest' value is 'False'
    # Input         : NA
    # Returned Type : NA
    # *************************************************************************************
    @staticmethod
    def exitTest(stopTest):
        if stopTest:
            GlobalFunction.stopExecution()
        else:
            pass
    # __________________________________________________________________________________________________________________

    # ************************************************************************************
    # Function Name : getUnDefinedObjDescription
    # Purpose       : To get the Object descripiton for which is not defined in 'Constant Description'.
    #                 Object description will be taken form 'stepDiscription'(globVal.stepDiscription) variable.
    #                 After fetching the descrioption, 'stepDiscription' variable value will set to default value('NA')
    # Input         : TestObject
    # Returned Type : String (Object Description)
    # *************************************************************************************
    @staticmethod
    def getUnDefinedObjDescription(webObject):
        if globVal.stepDiscription != 'NA':
            objDescription = str(globVal.stepDiscription)
            # The stepDiscription value will be re-set once step is updated in htmlCollector
            #globVal.stepDiscription = 'NA'
        else:
            objDescription = 'ObjectNameNotSet(stepDiscription variable In globalVariables)'

        return objDescription
    # __________________________________________________________________________________________________________________

    # ************************************************************************************
    # Function Name : getExceptionType
    # Purpose       : To get the name of the Exception Type
    # Input         : NA
    # Returned Type : String (Exception Name) or Exception Object
    # *************************************************************************************
    @staticmethod
    def getExceptionType():
        if globVal.exceptionType != 'NA':
            expType = str(globVal.exceptionType)
            globVal.exceptionType = 'NA'
        else:
            expType = 'ExceptionTypeNameNotSet'
        return expType
    # __________________________________________________________________________________________________________________

    # ************************************************************************************
    # Function Name : setExceptionType
    # Purpose       : To set the name of the Exception Type
    # Input         : Exception Object
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def setExceptionType(exceptionObject):
        try:
            globVal.exceptionType = str(type(exceptionObject).__name__)
            return True
        except Exception as e:
            return False

    # ########################################################################################
    # --------------------------- Common operational methods ----------------------------------
    # ########################################################################################

    # ************************************************************************************
    # Function Name : launchApplication
    # Purpose       : To launch the browser(Chrome or Firefox or IE) and navigate to specified URL
    # Input         : BrowserName, URL, waitTime
    # Returned Type : NA
    # *************************************************************************************
    @staticmethod
    def launchApplication(browserName, URL, setDriverDefaultWaitTime):
        stepName = "Open &lt;" + str(browserName) + "&gt; browser and navigating to &lt;"+str(URL)+'&gt;'
        defaultWaitTime = setDriverDefaultWaitTime
        try:
            if str(setDriverDefaultWaitTime).lower() == '':
                defaultWaitTime = 20
            else:
                defaultWaitTime = int(str(setDriverDefaultWaitTime).strip())

        except Exception as e:
            stepDetail = "Entered 'setDriverDefaultWaitTime' value is &lt;" + str(defaultWaitTime) + "&gt;. Expected 'Integer' or Empty 'String'."
            Report.customReport(stepName, stepDetail, "failed")
            GlobalFunction.stopExecution()
        try:
            if str(browserName).lower() == 'chrome':
                globVal.driver = Chrome(executable_path = "..\Drivers\chromedriver.exe")
            elif str(browserName).lower() == 'firefox':
                globVal.driver = Firefox(executable_path = "..\Drivers\geckodriver.exe")
            elif str(browserName).lower() == 'ie' or str(browserName).lower() == 'internetexplorer':
                globVal.driver = Ie(executable_path = "..\Drivers\IEDriverServer.exe")
            else:
                stepDetail = 'Entered &lt;'+str(browserName) +"&gt; browser is not implemented in the Framework. \
                            FYI, Framework supports 1)'Chrome', 2)'Firefox' & 3)'InternetExplore'."
                Report.customReport(stepName, stepDetail, "failed")
                GlobalFunction.stopExecution()

            globVal.driver.implicitly_wait(defaultWaitTime)
            globVal.driver.maximize_window()
            globVal.driver.get(URL)
            stepDetail = "&lt;"+str(browserName)+"&gt; browser opened successfully and navigated to &lt;" + str(URL)+"&gt;"
            Report.customReport(stepName, stepDetail, "passed")
        except Exception as e:
            stepDetail = "Encountered an issue. Error Type &lt;" + str(type(e).__name__) + "&gt; and Error description &lt;" + str(e) + "&gt;"
            Report.customReport(stepName, stepDetail, "failed")
            GlobalFunction.stopExecution()
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : closeAllBrowser
    # Purpose       : To close all the browsers opened by script
    # Input         : NA
    # Returned Type : NA
    # *************************************************************************************
    @staticmethod
    def closeAllBrowser(isScriptComplted):
        try:
            reportStep = "Close all browsers opened by script"
            globVal.driver.quit()

            if str(isScriptComplted).lower() == 'yes' or str(isScriptComplted).lower() == 'true':
                globVal.scriptCompletelyExecuted = 'Yes'
                Report.customReport(reportStep, "All browsers are closed", "Information")
                Report.saveHTMLReport()
                raise Exception('TestExecutionCompleted')
            elif str(isScriptComplted).lower() == 'no' or str(isScriptComplted).lower() == 'false':
                globVal.scriptCompletelyExecuted = 'No'
                Report.customReport(reportStep, "All browsers are closed", "Information")
            else:
                globVal.scriptCompletelyExecuted = 'Invalid Input'
                Report.customReport("closeAllBrowser(IsScriptComplted) function throwing warning", "Parameter value is not given correctly to 'closeAllBrowser(IsScriptCompleted) function'. [Entered: '" + isScriptComplted + "', Expected: 'True','False','Yes','No'] ", "warning")
                Report.customReport("Close all browsers opened by script", "All browsers are closed", "Information")
                Report.saveHTMLReport()
                raise Exception('TestExecutionStopped')
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                Report.customReport(reportStep, "All browsers are not closed, Error is : &lt;" + str(e) + "&gt;", "Failed")
                Report.saveHTMLReport()
                raise Exception('All browsers are not closed')
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : clickOnWebObj
    # Purpose       : To click web object in web page
    # Input         : webObject, expPage, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def clickOnWebObj(webObject, expPage, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webObject):
            testObjDescription = str(cnsLib.getObjDescription(webObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            if str(expPage).strip() == '':
                stepName = 'Click on &lt;' + str(testObjDescription) + '&gt;'
            else:
                stepName = 'Click on &lt;' + str(testObjDescription) + '&gt; and verify that the &lt;'+str(cnsLib.getObjDescription(expPage)) +'&gt; is displayed.'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webObject is Enabled
            if GlobalFunction.verifyWebObjEnabled(webObject,'',negativeReportStatus,stepName,waitTime,stopTest):
                # Verify 'webObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((webObject)):
                    # Get driver Object for webObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webObject,waitTime)
                # set passed webObject in function to testObj if object is not defined in constant library
                else:
                    testObj = webObject

                # Click on testObj
                testObj.click()

                # Verify page navigation if  'expPage' value is not Empty string('')
                if str(expPage).strip() != '':
                    if GlobalFunction.verifyNavigation(expPage,positiveReportStatus,negativeReportStatus,stepName,waitTime,stopTest):
                        return True
                    # expPage is not displayed
                    else:
                        return False
                else:
                    # Report Step if 'positiveReportStatus' value is not Empty String('')
                    if str(positiveReportStatus).strip() != '':
                        stepDetail = '&lt;' + testObjDescription + '&gt; is clicked'
                        Report.customReport(stepName, stepDetail, positiveReportStatus)
                    # testObj is clicked and return True
                    return True
            # webObject is not Enabled
            else:
                return False

        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is passed to function
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + testObjDescription + '&gt; is not clicked(ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : setDataToWebObj
    # Purpose       : To enter passed value into textbox in web page
    # Input         : webObject, webObjectValue, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def setDataToWebObj(webObject, webObjectValue, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webObject):
            testObjDescription = str(cnsLib.getObjDescription(webObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Enter the value &lt;'+str(webObjectValue)+'&gt; into  &lt;' +testObjDescription+ '&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webObject is Enabled
            if GlobalFunction.verifyWebObjEnabled(webObject,'',negativeReportStatus,stepName,waitTime,stopTest):
                # Verify 'webObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator(webObject):
                    # Get driver Object for webObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webObject,waitTime)
                # set passed webObject in function to testObj if object is not defined in constant library
                else:
                    testObj = webObject

                # set Passed webObjectvalue to webObject
                testObj.send_keys(webObjectValue)

                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail='The value &lt;'+str(webObjectValue) + '&gt; is entered into &lt;' + testObjDescription + '&gt;.'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                # testObj is clicked and return True
                return True
            # webObject is not Enabled
            else:
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is passed to function
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + str(webObjectValue) + "&gt; is not entered into &lt;" +testObjDescription+ '&gt;.(ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : verifyWebObjDisplayed
    # Purpose       : Verify WebObject is Displayed in web page
    # Input         : webObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def verifyWebObjDisplayed(webObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webObject):
            testObjDescription = str(cnsLib.getObjDescription(webObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Verify &lt;' + testObjDescription + '&gt; is displayed'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        # Verify 'webObject' value passed to function is defined in constant library
        if cnsLib.getObjLocator((webObject)):
            # Get driver Object for webObject
            if GlobalFunction.getDriverObjForWebObj(webObject,waitTime):
                testObj = GlobalFunction.getDriverObjForWebObj(webObject,waitTime)
            # webObject does not find in web page.
            else:
                # Report step if 'negativeReportStatus' is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + testObjDescription + '&gt; is not displayed [Exception Type: \'' + GlobalFunction.getExceptionType() + '\']'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
        # set passed webObject in function to testObj if object is not defined in constant library
        else:
            testObj = webObject

        try:
            # Verify testObj is displayed
            if testObj.is_displayed():
                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = '&lt;' + testObjDescription + '&gt; is displayed'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                # testObj is displayed and return True
                return True
            # testObj is not displayed
            else:
                # Report Step if negativeReportStatus value is passed to function
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + testObjDescription + '&gt; is not displayed [VerifyWebObjDisplayed]'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is passed to function
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + testObjDescription + '&gt; is not displayed(ExceptionType: &lt;'+exceptionType+'&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : verifyWebObjEnabled
    # Purpose       : Verify WebObject is Enabled in web page
    # Input         : webObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def verifyWebObjEnabled(webObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webObject):
            testObjDescription = str(cnsLib.getObjDescription(webObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Verify &lt;' + testObjDescription + '&gt; is Enabled'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webObject is Displayed
            if GlobalFunction.verifyWebObjDisplayed(webObject,'',negativeReportStatus,stepName,waitTime,stopTest):
                # Verify 'webObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((webObject)):
                    # Get driver Object for webObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webObject,waitTime)
                # set passed webObject in function to testObj if object is not defined in constant library
                else:
                    testObj = webObject

                # Check testObj is Enabled
                if testObj.is_enabled():
                    # Report Step if 'positiveReportStatus' value is not Empty String('')
                    if str(positiveReportStatus).strip() != '':
                        stepDetail = '&lt;' + testObjDescription + '&gt; is Enabled'
                        Report.customReport(stepName, stepDetail, positiveReportStatus)
                    # testObj is Enabled and return True
                    return True
                # testObj is not Enabled
                else:
                    # Report Step if 'negativeReportStatus' value is not Empty String('')
                    if str(negativeReportStatus).strip() != '':
                        stepDetail = '&lt;' + testObjDescription + '&gt; is not Enabled [VerifyWebObjEnabled]'
                        Report.customReport(stepName, stepDetail, negativeReportStatus)
                    # Exit Test if stopTest value is 'False'
                    GlobalFunction.exitTest(stopTest)
                    return False
            # webObject is not Displayed
            else:
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + testObjDescription + '&gt; is not Enabled(ExceptionType: &lt;'+exceptionType+'&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : verifyWebObjSelected
    # Purpose       : Verify WebObject is Selected in web page
    # Input         : webObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def verifyWebObjSelected(webObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webObject):
            testObjDescription = str(cnsLib.getObjDescription(webObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Verify &lt;' + testObjDescription + '&gt; is Selected'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webObject is Displayed
            if GlobalFunction.verifyWebObjDisplayed(webObject, '', negativeReportStatus, stepName, waitTime, stopTest):
                # Verify 'webObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((webObject)):
                    # Get driver Object for webObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webObject,waitTime)
                # set passed webObject in function to testObj if object is not defined in constant library
                else:
                    testObj = webObject

                # Check testObj is Selected
                if testObj.is_selected():
                    # Report Step if 'positiveReportStatus' value is not Empty String('')
                    if str(positiveReportStatus).strip() != '':
                        stepDetail = '&lt;' + testObjDescription + '&gt; is Selected'
                        Report.customReport(stepName, stepDetail, positiveReportStatus)
                    # testObj is Enabled and return True
                    return True
                # testObj is not Enabled
                else:
                    # Report Step if 'negativeReportStatus' value is not Empty String('')
                    if str(negativeReportStatus).strip() != '':
                        stepDetail = '&lt;' + testObjDescription + '&gt; is not Selected [VerifyWebObjSelected]'
                        Report.customReport(stepName, stepDetail, negativeReportStatus)
                    # Exit Test if stopTest value is 'False'
                    GlobalFunction.exitTest(stopTest)
                    return False
            # webObject is not Displayed
            else:
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + testObjDescription + '&gt; is not Selected(ExceptionType: &lt;'+exceptionType+ '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : verifyNavigation
    # Purpose       : Verify expected page is displayed in web page
    # Input         : expPage, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def verifyNavigation(expPage, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # Verify 'expPage' value passed to function is defined in constant library
        if cnsLib.getObjLocator(expPage):
            # set Object name of 'expObject' to 'testObj'
            testObj = cnsLib.getObjLocator(expPage)
            # Get Object description
            if cnsLib.getObjDescription(expPage):
                testObjDescription = str(cnsLib.getObjDescription(expPage))
            # Get Object description for undefined webObject in constant library
            else:
                testObjDescription = 'PageNameNotDefined'
        # 'expPage' is not defined in constant library(under 'getObjLocator(object)')
        else:
            # Report Step if 'negativeReportStatus' value is not Empty String('')
            if str(negativeReportStatus).strip() != '':
                if reportStep == '':
                    stepName = "Verify &lt;"+str(expPage)+"&gt; is displayed"
                else:
                    stepName = reportStep
                stepDetail = "&lt;"+str(expPage)+"&gt; is not defined in constant library(under 'getObjLocator(object)') [verifyNavigation]"
                Report.customReport(stepName, stepDetail, negativeReportStatus)
            # Exit Test if stopTest value is 'False'
            GlobalFunction.exitTest(stopTest)
            return False

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Verify &lt;' + testObjDescription + '&gt; is displayed'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify 'expPage' is Displayed
            if GlobalFunction.verifyWebObjDisplayed(testObj, '', '', stepName, waitTime, False):
                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = '&lt;' + testObjDescription + '&gt; is displayed'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                # 'expPage' is Displayed
                return True

            # 'expPage' is not Displayed
            else:
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + testObjDescription + '&gt; is not displayed [verifyNavigation]'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'True'
                GlobalFunction.exitTest(stopTest)
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + testObjDescription + '&gt; is not displayed(ExceptionType: &lt;'+exceptionType+'&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : verifyItemInWebList
    # Purpose       : To check given value exist in web list.
    # Input         : webObject, dropdownValue, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def verifyItemInWebList(webObject, webObjectValue, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webObject):
            testObjDescription = str(cnsLib.getObjDescription(webObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Verify &lt;'+str(webObjectValue)+'&gt; is present in &lt;' + testObjDescription + '&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webObject is Displayed
            if GlobalFunction.verifyWebObjEnabled(webObject, '', negativeReportStatus, stepName, waitTime, stopTest):
                # Verify 'webObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((webObject)):
                    # Get driver Object for webObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webObject, waitTime)
                # set passed webObject in function to testObj if object is not defined in constant library
                else:
                    testObj = webObject

                # Verify given webObjectValue present in webList
                listItems = testObj.find_elements_by_xpath("//option")
                for item in listItems:
                    value = str(item.text).strip()
                    if value == str(webObjectValue):
                        # Report Step if 'positiveReportStatus' value is not Empty String('')
                        if str(positiveReportStatus).strip() != '':
                            stepDetail = '&lt;'+str(webObjectValue)+'&gt; is present in &lt;' + testObjDescription + '&gt;'
                            Report.customReport(stepName, stepDetail, positiveReportStatus)
                        return True
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;'+str(webObjectValue)+'&gt; is not present in &lt;' + testObjDescription + '&gt;[verifyItemInWebList]'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False

            # webObject is not Enabled
            else:
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;'+str(webObjectValue)+'&gt; is not present in &lt;'+testObjDescription+'&gt;(ExceptionType: &lt;'+exceptionType+'&gt;)[verifyItemInWebList]'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------
    # ************************************************************************************
    # Function Name : selectDropdownWebObjValByName
    # Purpose       : Select value from dropdown webObject
    # Input         : webObject, dropdownValue, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def selectDropdownWebObjValByName(webObject, dropdownValue, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webObject):
            testObjDescription = str(cnsLib.getObjDescription(webObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Select &lt;' + str(dropdownValue) + '&gt; in &lt;' + testObjDescription + '&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify dropdownValue is present webObject
            if GlobalFunction.verifyItemInWebList(webObject, dropdownValue, '', negativeReportStatus, stepName,waitTime,stopTest):
                # Verify 'webObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((webObject)):
                    # Get driver Object for webObject
                    testObj = Select(GlobalFunction.getDriverObjForWebObj(webObject, waitTime))
                # set passed webObject in function to testObj if object is not defined in constant library
                else:
                    testObj = Select(webObject)

                # Select passed dropdown value
                testObj.select_by_visible_text(str(dropdownValue).strip())
                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = '&lt;' + str(dropdownValue) + '&gt; is selected in &lt;' + testObjDescription + '&gt;'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                return True

            #  dropdownValue not found in webObjectList
            else:
                return False

        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + str(dropdownValue) + '&gt; is not selected in &lt;' + testObjDescription + '&gt;(ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception

    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : selectDropdownWebObjValByIndex
    # Purpose       : Select value from dropdown webObject
    # Input         : webObject, dropdownValue, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def selectDropdownWebObjValByIndex(webObject, dropdownValue, positiveReportStatus, negativeReportStatus,
                                      reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webObject):
            testObjDescription = str(cnsLib.getObjDescription(webObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Select &lt;' + str(dropdownValue) + '&gt; index value in &lt;' + testObjDescription + '&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webObject is Enabled
            if GlobalFunction.verifyWebObjEnabled(webObject, '', negativeReportStatus, stepName, waitTime, stopTest):
                # Verify 'webObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((webObject)):
                    # Get driver Object for webObject
                    testObj = Select(GlobalFunction.getDriverObjForWebObj(webObject, waitTime))
                # set passed webObject in function to testObj if object is not defined in constant library
                else:
                    testObj = Select(webObject)

                # Select passed dropdown value
                testObj.select_by_index(int(dropdownValue))
                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = '&lt;' + str(dropdownValue) + '&gt; index value is selected in &lt;' + testObjDescription + '&gt;'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                return True

            #  webObject is not enabled
            else:
                return False

        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = '&lt;' + str(
                        dropdownValue) + '&gt; index value is not selected in &lt;' + testObjDescription + '&gt;(ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception

    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : selectValsFromListboxWebObj
    # Purpose       : Select multiple values from Listbox webObject
    # Input         : listboxValues_SeperatedBySemicolon, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    #
    # Note : All listbox values should be defined in constant library
    # *************************************************************************************
    @staticmethod
    def selectValsFromListboxWebObj(listboxValues_SeperatedBySemicolon, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        try:
            object_Names = ''
            valuesList = str(listboxValues_SeperatedBySemicolon).split(';')
            for obj in valuesList:
                object_Names += str(cnsLib.getObjDescription(obj)) + ', '
            else:
                object_Names = object_Names[:-2]
            if reportStep.lower() == 'stepname':
                reportStep = 'Select "' + str(object_Names) + '" values from Listbox'
            for obj in valuesList:
                ActionChains(globVal.driver).key_down(Keys.CONTROL).click(GlobalFunction.getDriverObjForWebObj(obj,waitTime)).key_up(Keys.CONTROL).perform()
            Report.customReport(reportStep, '"' + str(object_Names) + '" are selected from Listbox', positiveReportStatus)
            return True
        except NoSuchElementException as exception:
            Report.customReport(reportStep, '"' + str(object_Names) + '" are not selected from Listbox(No such element found)', negativeReportStatus)
            GlobalFunction.exitTest(stopTest)
            return False
        except Exception as e:
            Report.customReport(reportStep, '"' + str(object_Names) + '" are not selected from Listbox', negativeReportStatus)
            GlobalFunction.exitTest(stopTest)
            return False
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : getWebObjAttributeValue
    # Purpose       : Get Attribute value of WebObject
    # Input         : webObject, attributeName, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : String(str) or False(bool)
    # *************************************************************************************
    @staticmethod
    def getWebObjAttributeValue(webObject, attributeName, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webObject):
            testObjDescription = str(cnsLib.getObjDescription(webObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Get Attribute value of &lt;' + str(attributeName) + '&gt; from &lt;' + str(testObjDescription) + '&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webObject is Displayed
            if GlobalFunction.verifyWebObjDisplayed(webObject, '', negativeReportStatus, stepName, waitTime, stopTest):
                # Verify 'webObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((webObject)):
                    # Get driver Object for webObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webObject, waitTime)
                # set passed webObject in function to testObj if object is not defined in constant library
                else:
                    testObj = webObject

                # Get total column count of webTable
                attributeValue = testObj.get_attribute(str(attributeName))

                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = 'Attribute Value&lt;' + attributeValue + '&gt; is retrived from &lt;' + testObjDescription + '&gt;'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                return attributeValue
            # webObject is not Displayed
            else:
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'Attribute Value is not retrived from &lt;'+ testObjDescription + '&gt; (ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : getDataFromDataSheet
    # Purpose       : Get Data from the Excel
    # Input         : filePath, sheetName, rowName, columnName, positiveReportStatus, negativeReportStatus, reportStep, stopTest, matchedRowCount
    # Returned Type : String(str) or False(bool)
    # *************************************************************************************
    @staticmethod
    def getDataFromDataSheet(filePath, sheetName, rowName, columnName, positiveReportStatus, negativeReportStatus, reportStep, stopTest, matchedRowCount):
        # Define filePath variable
        if str(filePath).strip() == '':
            filePath = globVal.testData_ExcelPath

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Fetch data from DataSheet(File Path:&lt;'+str(filePath)+'&gt;)'
        else:
            stepName = reportStep

        try:
            # Defining 'matchedRowCount'
            if str(matchedRowCount).strip() == '':
                matchedRowCount = 1
            else:
                matchedRowCount = int(matchedRowCount)

            # Created Excel object using 'openpyxl' and get data from dataSheet
            wb = openpyxl.load_workbook(filename=filePath, read_only=True)
            sh = wb[sheetName]
            maxRow = sh.max_row
            maxColumn = sh.max_column
            reqRowNum = 1
            reqColumNum = 1
            machedCount = 1
            for r in range(1, maxRow + 1):
                if str(sh.cell(r, 1).value).lower() == str(rowName).lower():
                    if machedCount == int(matchedRowCount):
                        reqRowNum = r
                        break
                    else:
                        machedCount+=1
                else:
                    if r == maxRow:
                        # Report Step if 'negativeReportStatus' value is not Empty String('')
                        if str(negativeReportStatus).strip() != '':
                            stepDetail = 'Entered row name&lt;' + str(rowName) + '&gt; is not found in given sheet name&lt;'+str(sheetName)+'&gt;'
                            Report.customReport(stepName, stepDetail, negativeReportStatus)
                        # Exit Test if stopTest value is 'False'
                        GlobalFunction.exitTest(stopTest)
                        return False
            for c in range(1, maxColumn + 1):
                if str(sh.cell(1, c).value).lower() == str(columnName).lower():
                    reqColumNum = c
                    break
                else:
                    if c == maxColumn:
                        # Report Step if 'negativeReportStatus' value is not Empty String('')
                        if str(negativeReportStatus).strip() != '':
                            stepDetail = 'Entered column name&lt;' + str(columnName) + '&gt; is not found in given sheet name&lt;'+str(sheetName)+'&gt;'
                            Report.customReport(stepName, stepDetail, negativeReportStatus)
                        # Exit Test if stopTest value is 'False'
                        GlobalFunction.exitTest(stopTest)
                        return False
            requiredData = sh.cell(reqRowNum, reqColumNum).value
            wb._archive.close()
            # Report Step if 'positiveReportStatus' value is not Empty String('')
            if str(positiveReportStatus).strip() != '':
                stepDetail = '&lt;' + str(requiredData) + '&gt; value is taken from DataSheet'
                Report.customReport(stepName, stepDetail, positiveReportStatus)
            return str(requiredData)

        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'Data not fetched from DataSheet. (ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------
    #################################################
    # ************************************************************************************
    # Function Name : getCellDataFromWebTable
    # Purpose       : Get cell data of given row & column numbers in webTable
    # Input         : webTableObject, rowNumber, columnNumber, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : String(str) or False(bool)
    # *************************************************************************************
    @staticmethod
    def getCellDataFromWebTable(webTableObject, rowNumber, columnNumber, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webTableObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webTableObject):
            testObjDescription = str(cnsLib.getObjDescription(webTableObject))
        # Get Object description for undefined webTableObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webTableObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Get cell data of &lt;' + testObjDescription + '&gt; from row &lt;' + str(
                rowNumber) + '&gt; and column &lt;' + str(columnNumber) + '&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify cell exist in webTable with given co-ordinates
            if GlobalFunction.verifyWebTableCellExist(webTableObject,rowNumber,columnNumber,'',negativeReportStatus,stepName,waitTime,stopTest):
                # Verify 'webTableObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator(webTableObject):
                    # Get driver Object for webTableObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webTableObject, waitTime)
                # set passed webTableObject in function to testObj if webTableObject is not defined in constant library
                else:
                    testObj = webTableObject

                cellData = testObj.find_element_by_xpath("//tr[" + str(rowNumber) + "]/td[" + str(columnNumber) + "]").text
                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = '&lt;' + str(cellData) + '&gt; is retrived from &lt;' + testObjDescription + '&gt;'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                # testObj is Enabled and return True
                return str(cellData)
            # Cell doesn't exist with given co-ordinates in webObject
            else:
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'Cell data not retrived from &lt;' + testObjDescription + '&gt; (ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : verifyWebTableCellExist
    # Purpose       : Verify cell exist in the passed webtable
    # Input         : webTableObject, rowNumber, columnNumber, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def verifyWebTableCellExist(webTableObject, rowNumber, columnNumber, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webTableObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webTableObject):
            testObjDescription = str(cnsLib.getObjDescription(webTableObject))
        # Get Object description for undefined webTableObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webTableObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Verify the cell exist in &lt;'+testObjDescription+'&gt; from row &lt;'+str(rowNumber)+'&gt; and column &lt;'+str(columnNumber)+'&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        # Verify passed rowNumber and columnNumber values are valid
        try:
            int(rowNumber);int(columnNumber)
        except Exception:
            # Report Step if 'negativeReportStatus' value is not Empty String('')
            if str(negativeReportStatus).strip() != '':
                stepDetail = 'Given co-ordinates(row&lt;' + str(rowNumber) + '&gt; and/or &lt;' + str(columnNumber) + "&gt;) are invalid"
                Report.customReport(stepName, stepDetail, negativeReportStatus)
            # Exit Test if stopTest value is 'False'
            GlobalFunction.exitTest(stopTest)
            return False
        try:
            #get total row and column count of webTable
            rowCount = GlobalFunction.getRowCountOfWebTable(webTableObject,'',negativeReportStatus,stepName,waitTime,stopTest)
            columnCount = GlobalFunction.getColumnCountOfWebTable(webTableObject,'',negativeReportStatus,stepName,waitTime,stopTest)

            # Check rows and columns values are valid
            if not rowCount or not columnCount:
                # rows or columns are not found
                return False

            # Verify given row and column numbers are not exist in webTable
            if rowCount < int(rowNumber) or columnCount < int(columnNumber):
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'In &lt;' + testObjDescription + '&gt; Cell with given co-ordinates(row&lt;'+str(rowNumber)+'&gt; and &lt;'+str(columnNumber)+"&gt;) is not exist."
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            # Given cell with row and column number is exist
            else:
                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = 'In &lt;' + testObjDescription + '&gt; Cell with given co-ordinates(row&lt;'+str(rowNumber)+'&gt; and &lt;'+str(columnNumber)+"&gt;) is exist."
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                return True
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'In &lt;' + testObjDescription + '&gt; Cell with given co-ordinates(row&lt;'+str(rowNumber)+'&gt; and &lt;'+str(columnNumber)+"&gt;) is not exist.(ExceptionType: &lt;" + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : getChildObjOfWebTable
    # Purpose       : Get cell object of given row & column numbers in webTable
    # Input         : webTableObject, rowNumber, columnNumber, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : 'selenium driver object' or 'False(bool)'
    # *************************************************************************************
    @staticmethod
    def getChildObjOfWebTable(webTableObject, rowNumber, columnNumber, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webTableObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webTableObject):
            testObjDescription = str(cnsLib.getObjDescription(webTableObject))
        # Get Object description for undefined webTableObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webTableObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Verify the cell exist in &lt;' + testObjDescription + '&gt; from row &lt;' + str(
                rowNumber) + '&gt; and column &lt;' + str(columnNumber) + '&gt;'
            stepName = 'In &lt;'+testObjDescription+'&gt;, Get Object of cell with give co-ordinates(Row&lt;'+str(rowNumber)+'&gt; & Column&lt;'+str(columnNumber)+'&gt;)'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify cell exist in webTable with given co-ordinates
            if GlobalFunction.verifyWebTableCellExist(webTableObject, rowNumber, columnNumber, '', negativeReportStatus,
                                                      stepName, waitTime, stopTest):
                # Verify 'webTableObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator(webTableObject):
                    # Get driver Object for webTableObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webTableObject, waitTime)
                # set passed webTableObject in function to testObj if webTableObject is not defined in constant library
                else:
                    testObj = webTableObject

                chaildObj = testObj.find_element_by_xpath("//tr[" + str(rowNumber) + "]/td[" + str(columnNumber) + "]")

                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = 'Child Object is retrived from &lt;' + testObjDescription + '&gt;'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                # return child object
                return chaildObj
            # Cell doesn't exist with given co-ordinates in webObject
            else:
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'Child Object is not retrived from &lt;' + testObjDescription + '&gt; (ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : getRowCountOfWebTable
    # Purpose       : Get total rows count of webTable
    # Input         : webTableObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : Integer(int) or False(bool)
    # *************************************************************************************
    @staticmethod
    def getRowCountOfWebTable(webTableObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webTableObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webTableObject):
            testObjDescription = str(cnsLib.getObjDescription(webTableObject))
        # Get Object description for undefined webTableObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webTableObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Get row count of &lt;' + testObjDescription + '&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webTableObject is Displayed
            if GlobalFunction.verifyWebObjDisplayed(webTableObject, '', negativeReportStatus, stepName, waitTime,stopTest):
                # Verify 'webTableObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((webTableObject)):
                    # Get driver Object for webTableObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webTableObject, waitTime)
                # set passed webTableObject in function to testObj if webTableObject is not defined in constant library
                else:
                    testObj = webTableObject

                # Get total row count of webTable
                rows = len(testObj.find_elements_by_xpath("//tr"))

                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = 'Row count&lt;'+str(rows)+'&gt; is retrived from &lt;' + testObjDescription + '&gt;'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                # testObj is Enabled and return True
                return rows
            # webTableObject is not Displayed
            else:
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'Row count not retrived from &lt;' + testObjDescription + '&gt; (ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : getColumnCountOfWebTable
    # Purpose       : Get total columns count of webTable
    # Input         : webTableObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : Integer(int) or False(bool)
    # *************************************************************************************
    @staticmethod
    def getColumnCountOfWebTable(webTableObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webTableObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webTableObject):
            testObjDescription = str(cnsLib.getObjDescription(webTableObject))
        # Get Object description for undefined webTableObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webTableObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Get column count of &lt;' + testObjDescription + '&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webTableObject is Displayed
            if GlobalFunction.verifyWebObjDisplayed(webTableObject, '', negativeReportStatus, stepName, waitTime, stopTest):
                # Verify 'webTableObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((webTableObject)):
                    # Get driver Object for webTableObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webTableObject, waitTime)
                # set passed webTableObject in function to testObj if object is not defined in constant library
                else:
                    testObj = webTableObject

                # Get total column count of webTable
                columnCount = len(testObj.find_elements_by_xpath("//tr[1]/th"))

                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = 'Column count&lt;' + str(columnCount) + '&gt; is retrived from &lt;' + testObjDescription + '&gt;'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                return columnCount
            # webTableObject is not Displayed
            else:
                return False
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'Column count not retrived from &lt;' + testObjDescription + '&gt; (ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : getTotalDataOfWebTable
    # Purpose       : To get total data in webTable
    # Input         : webTableObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : String(str) or False(bool)
    # *************************************************************************************
    @staticmethod
    def getTotalDataOfWebTable(webTableObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webTableObject):
            testObjDescription = str(cnsLib.getObjDescription(webTableObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webTableObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Get Total Data in &lt;' + testObjDescription + '&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # get total row and column count of webTable
            rows = GlobalFunction.getRowCountOfWebTable(webTableObject, '', negativeReportStatus, stepName,waitTime, stopTest)
            cols = GlobalFunction.getColumnCountOfWebTable(webTableObject, '', negativeReportStatus, stepName, waitTime, stopTest)
            # Check rows and columns values are valid
            if not rows or not cols:
                #rows or columns are not found
                return False
            # Verify 'webObject' value passed to function is defined in constant library
            if cnsLib.getObjLocator((webTableObject)):
                # Get driver Object for webObject
                testObj = GlobalFunction.getDriverObjForWebObj(webTableObject, waitTime)
            # set passed webObject in function to testObj if object is not defined in constant library
            else:
                testObj = webTableObject

            allData = []
            for r in range(1, rows + 1):
                rowData = []
                for c in range(1, cols + 1):
                    if r == 1:
                        rowData.append(testObj.find_element_by_xpath("//tr[" + str(r) + "]/th[" + str(c) + "]").text)
                    else:
                        rowData.append(testObj.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(c) + "]").text)
                allData.append(rowData)

            # Report Step if 'positiveReportStatus' value is not Empty String('')
            if str(positiveReportStatus).strip() != '':
                stepDetail = 'Total data in &lt;' + testObjDescription + '&gt; is retrived'
                Report.customReport(stepName, stepDetail, positiveReportStatus)
            return str(allData)

        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is not Empty String('')
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'Total Data is not retrived from &lt;' + testObjDescription + '&gt; .(ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : switchWindowByIndex
    # Purpose       : To switch between the browser windows
    # Input         : indexNum, positiveReportStatus, negativeReportStatus, reportStep, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def switchWindowByIndex(indexNum, positiveReportStatus, negativeReportStatus, reportStep, stopTest):
        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Switch the driver focus to new window&lt;Index No:' + str(indexNum) + '&gt;'
        else:
            stepName = reportStep
        try:
            indexNum = int(str(indexNum).strip())
        except:
            # Report Step if 'negativeReportStatus' value is passed to function
            if str(negativeReportStatus).strip() != '':
                stepDetail = 'Invalid indexNumber&lti.e: ;' + str(
                    indexNum) + '&gt; passed to the function[switchWindowByIndex]'
                Report.customReport(stepName, stepDetail, negativeReportStatus)
            # Exit Test if stopTest value is 'False'
            GlobalFunction.exitTest(stopTest)
            return False
        try:
            new_window = globVal.driver.window_handles[int(str(indexNum).strip())]
            globVal.driver.switch_to.window(new_window)
            # Report Step if 'positiveReportStatus' value is not Empty String('')
            if str(positiveReportStatus).strip() != '':
                stepDetail = 'driver focus is switched to new window&lt;Index No:' + str(indexNum) + '&gt;'
                Report.customReport(stepName, stepDetail, positiveReportStatus)
            # driver focus is switched
            return True
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is passed to function
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'driver focus is not swiched to new window(ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : switchToAlert
    # Purpose       : To get the message in alerts and click on 'Ok' button or close the alert box.
    # Input         : acceptAlert, getAlertMessage, positiveReportStatus, negativeReportStatus, reportStep, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def switchToSimpleAlert(acceptAlert, getAlertMessage, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        if not(isinstance(acceptAlert,bool)) or not(isinstance(getAlertMessage, bool)):
            # Report Step if 'negativeReportStatus' value is passed to function
            if str(negativeReportStatus).strip() != '':
                stepDetail = 'Invalid parameters passed to passed to the function[switchToSimpleAlert]'
                Report.customReport(str(reportStep), stepDetail, negativeReportStatus)
            # Exit Test if stopTest value is 'False'
            GlobalFunction.exitTest(stopTest)
            return False
        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            if acceptAlert == True:
                if getAlertMessage == True:
                    stepName = 'Get message displayed in the alert box and click on "OK" button'
                else:
                    stepName = 'Click on "OK" button in alert box'
            else:
                if getAlertMessage == True:
                    stepName = 'Get message displayed in the alert box and close the popup'
                else:
                    stepName = 'Close the alert box'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20
        #Handling simple alert
        try:
            WebDriverWait(globVal.driver, int(waitTime)).until(EC.alert_is_present(),'confirmation popup to appear.')
            alert = globVal.driver.switch_to.alert
            if getAlertMessage == True:
                message = alert.text
            if acceptAlert == True:
                alert.accept()
            else:
                alert.dismiss()
            # Report Step if 'positiveReportStatus' value is not Empty String('')
            if str(positiveReportStatus).strip() != '':
                if acceptAlert == True:
                    if getAlertMessage == True:
                        stepDetail = 'Message&lt;'+str(message)+'&gt; retrived and "OK" button is clicked in alert box'
                    else:
                        stepDetail = '"OK" button is clicked in alert box'
                else:
                    if getAlertMessage == True:
                        stepDetail = 'Message&lt;'+str(message)+'&gt; retrived and closed alert box'
                    else:
                        stepDetail = 'Alert box is closed'
                Report.customReport(stepName, stepDetail, positiveReportStatus)
            if getAlertMessage == True:
                return message
            else:
                return True
        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is passed to function
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'Not able to handle Alert box(ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : mouseHoverOnWebObj
    # Purpose       : To hover the mouse pointer on webObject
    # Input         : webObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def mouseHoverOnWebObj(webObject, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'webObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(webObject):
            testObjDescription = str(cnsLib.getObjDescription(webObject))
        # Get Object description for undefined webObject in constant library
        else:
            testObjDescription = str(GlobalFunction.getUnDefinedObjDescription(webObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            stepName = 'Hover the mouse pointer on &lt;' + str(testObjDescription) + '&gt;'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webObject is Enabled
            if GlobalFunction.verifyWebObjEnabled(webObject, '', negativeReportStatus, stepName, waitTime, stopTest):
                # Verify 'webObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((webObject)):
                    # Get driver Object for webObject
                    testObj = GlobalFunction.getDriverObjForWebObj(webObject, waitTime)
                # set passed webObject in function to testObj if object is not defined in constant library
                else:
                    testObj = webObject

                # Hover the mouse on passed webObject
                action = ActionChains(globVal.driver).move_to_element(testObj)
                action.perform()

                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = 'Mouse hovered on &lt;' + testObjDescription + '&gt;'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                # Mouse hovered and return True
                return True
            # webObject is not Enabled
            else:
                return False

        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is passed to function
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'Mouse is not hovered on &lt;' + testObjDescription + '&gt;(ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------

    # ************************************************************************************
    # Function Name : uploadFile
    # Purpose       : To upload the file in webPage
    # Input         : fileObject, submitBtnObject, filePath, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest
    # Returned Type : bool(True or False)
    # *************************************************************************************
    @staticmethod
    def uploadFile(fileObject, submitBtnObject, filePath, positiveReportStatus, negativeReportStatus, reportStep, waitTime, stopTest):
        # If 'fileObject' value passed to function is defined in constant library, Get Object description
        if cnsLib.getObjLocator(fileObject):
            fileObjDescription = str(cnsLib.getObjDescription(fileObject))
        # Get Object description for undefined webObject in constant library
        else:
            fileObjDescription = str(GlobalFunction.getUnDefinedObjDescription(fileObject))

        # Defining 'stepName' variable
        if str(reportStep).strip() == '':
            if str(submitBtnObject).strip() == '':
                stepName = 'Browse the file&lt;'+ str(filePath)+'&gt; to &lt;' + str(fileObjDescription) + '&gt;'
            else:
                stepName = 'Browse the file&lt;'+ str(filePath)+'&gt; to &lt;' + str(fileObjDescription) + '&gt; and upload it'
        else:
            stepName = reportStep

        # Defining 'waitTime' variable
        try:
            waitTime = int(str(waitTime).strip())
        except Exception:
            waitTime = 20

        try:
            # Verify webObject is Enabled
            if GlobalFunction.verifyWebObjEnabled(fileObject, '', negativeReportStatus, stepName, waitTime, stopTest):
                # Verify 'fileObject' value passed to function is defined in constant library
                if cnsLib.getObjLocator((fileObject)):
                    # Get driver Object for webObject
                    testObj = GlobalFunction.getDriverObjForWebObj(fileObject, waitTime)
                # set passed webObject in function to testObj if object is not defined in constant library
                else:
                    testObj = fileObject

                # set Passed webObjectvalue to webObject
                testObj.send_keys(str(filePath))

                # check submit button object passed
                if str(submitBtnObject).strip() != '':
                    # Verify 'submitBtnObject' value passed to function is defined in constant library
                    if cnsLib.getObjLocator((submitBtnObject)):
                        # Get driver Object for webObject
                        testObj = GlobalFunction.getDriverObjForWebObj(submitBtnObject, waitTime)
                    # set passed webObject in function to testObj if object is not defined in constant library
                    else:
                        testObj = submitBtnObject
                    # Clicking on submit or Upload button
                    testObj.click()
                # Report Step if 'positiveReportStatus' value is not Empty String('')
                if str(positiveReportStatus).strip() != '':
                    stepDetail = 'File uploaded successfully to &lt;' + fileObjDescription + '&gt;'
                    Report.customReport(stepName, stepDetail, positiveReportStatus)
                # testObj is clicked and return True
                return True
            # webObject is not Enabled
            else:
                return False

        # Catch if Exception is occurred
        except Exception as e:
            exceptionType = str(type(e).__name__)
            if exceptionType.lower() != 'exception':
                # Report Step if 'negativeReportStatus' value is passed to function
                if str(negativeReportStatus).strip() != '':
                    stepDetail = 'File not uploaded successfully to &lt;'+fileObjDescription +'&gt; (ExceptionType: &lt;' + exceptionType + '&gt;)'
                    Report.customReport(stepName, stepDetail, negativeReportStatus)
                # Exit Test if stopTest value is 'False'
                GlobalFunction.exitTest(stopTest)
                return False
            else:
                raise Exception
    # ------------------------------------------------------------------------------------------------------------------
