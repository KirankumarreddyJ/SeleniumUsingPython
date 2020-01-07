
class GlobalVariables:
    driver = None
    batchFlow_ExcelPath = "../Batchflow/Batchflow.xlsx"
    batchFlow_TestCases_SheetName = 'TestCases'
    testData_ExcelPath = "../TestData/TestData.xlsx"
    testData_TestData_SheetName = "TestData"
    testData_Credentials_SheetName = "Credentials"
    testData_URLs_SheetName = "URLs"
    testerInfo = 'J Kirankumarredddy'
    scriptCompletelyExecuted = 'No'
    testBrowserName = ''
    testURL = ''
    testCaseName =   ''
    testStartTime = ''
    testEndTime = ''
    testDuration =   ''
    testType     =   ''
    testResultFolderName = ''
    testResultFolderPath   = ''
    batchResultPath = ''
    batchResultExcelPath = ''
    stepName  =   ''
    stepDiscription = 'NA'
    exceptionType = 'NA'
    exitTestOnStepFail = True
    dontExitTestOnStepFail = False
    stepNumber   =0
    totalPassed  =0
    totalFailed  =0
    totalWarning =0
    totalSteps   =0
    totalInformation =0
    screenshotCount =0

    @staticmethod
    def resetGlobalVals():
        GlobalVariables.stepNumber = 0
        GlobalVariables.totalPassed = 0
        GlobalVariables.totalFailed = 0
        GlobalVariables.totalWarning = 0
        GlobalVariables.totalSteps = 0
        GlobalVariables.totalInformation = 0
        GlobalVariables.screenshotCount = 0



