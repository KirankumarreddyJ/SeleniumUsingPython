import os
import sys
import time
from datetime import datetime
from FunctionLibrery.globalVariables import GlobalVariables as globVal



class Report():
    global htmlCollector
    def __init__(self):
        globVal.testStartTime = datetime.now().strftime("%d-%b-%y %I:%M:%S %p")
        Report.makeTestResultDirectory()
        Report.genHTMLReport()
    @staticmethod
    def makeTestResultDirectory():
        globVal.testResultFolderName = globVal.testCaseName + '_' + time.strftime("%Y%m%d-%H%M%S")
        globVal.testResultFolderPath = "../Results/TestResults/" + globVal.testResultFolderName
        try:
            os.makedirs(globVal.testResultFolderPath)
        except OSError:
            print("Creation of the directory %s failed" % globVal.testResultFolderPath)
            raise Exception("Creation of the directory '" + str(globVal.testResultFolderPath) + "' failed")
            #sys.exit(1)
    @staticmethod
    def takeScreenshot():
        try:
            # Take Screenshot and Return True
            globVal.screenshotCount += 1
            globVal.driver.save_screenshot(globVal.testResultFolderPath + '/' + str(globVal.screenshotCount) + '.png')
            return True
        except Exception:
            # Return False if Screenshot Not Captured
            globVal.screenshotCount -= 1
            return False
    @staticmethod
    def genHTMLReport():
        global htmlCollector
        htmlCollector = '<html><head><style>' \
                   'table, th, td {' \
                        'border: 2px solid black;' \
                        'border-collapse: collapse;' \
                        'text-align: left;}' \
                   'th, td { ' \
                        'padding: 3px;}' \
                   'h2{ text-align: center;}'\
                   'table#t01,table#t02 {' \
                        'width:60%;' \
                    ' background-color: #f1f1c1;}' \
                   '</style></head>'
        # Creating Header of Report
        htmlCollector = htmlCollector + '<body bgcolor="#E6E6FA"><h2>AUTOMATION TEST RESULTS</h2>' \
                                        '<table align="center" id="t01"><tr><th width="28%">Test Case Name:</th><td>'+globVal.testCaseName+'</td></tr></table>' \
                                        '<p></p>' \
                                        \
                                        '<table align="center" id="t02">' \
                                        '<tr><th>Test Started:</th><td>'+globVal.testStartTime+'</td><th width="27%">Test Type:</th><td>'+globVal.testType+'</td></tr>' \
                                        '<tr><th>Test Ended:</th><td>testEndTime</td><th>Browser Name:</th><td>'+globVal.testBrowserName+'</td></tr>' \
                                        '<tr><th>Test Duration:</th><td>testDuration</td><th></th><td></td></tr>'\
                                        '<tr><th style="color:#2EAF2E">Total Passed:</th><td style="color:#2EAF2E">totalPassed</td><th>Total Steps:</th><td>totalSteps</td></tr>' \
                                        '<tr><th style="color:#FF0000">Total Failed:</th><td style="color:#FF0000">totalFailed</td><th>Total Information:</th><td>totalInformation</td></tr>' \
                                        '<tr><th style="color:#8b2323">Total Warnings:</th><td style="color:#8b2323">totalWarnings</td><th>Script Completely Executed:</th><td>scriptCompletelyExecuted</td></tr></table><p></p>'
        # Creating Column names of test steps
        htmlCollector = htmlCollector + '<table style="width:100%"><tr bgcolor="#99ff66">' \
                                        '<th style="text-align:center" width="8%">Step Number</th>' \
                                        '<th style="text-align:center">Step Name</th>' \
                                        '<th style="text-align:center">Actual Result</th>' \
                                        '<th style="text-align:center" width="10%">Step Status</th>' \
                                        '<th style="text-align:center" width="13%">Time of Execution</th>' \
                                        '<th style="text-align:center" width="10%">Error Screen shot</th></tr>'
                                        #'</table></body>'
    @staticmethod
    def getCurrentTime():
        now = datetime.now()
        return str(now.strftime("%I:%M:%S %p"))
    @staticmethod
    def getCurrentDateAndTime():
        now = datetime.now()
        return str(now.strftime("%d-%b-%y %I:%M:%S %p"))

    @staticmethod
    def getTestEndTime():
        testEndTime = datetime.now().strftime("%d-%b-%y %I:%M:%S %p")
        return testEndTime
    @staticmethod
    def customReportStepNum(StepNumber, StepDescription):
        global htmlCollector
        htmlCollector = htmlCollector + '<tr><td style="text-align:center">Step ' + str(StepNumber) +'</td><td>' + StepDescription + '</td><td></td>' +'<td style="text-align:center";>Information</td><td style="text-align:center">' + Report.getCurrentTime() + '</td><td></td></tr>'
        globVal.totalInformation += 1
        globVal.totalSteps+=1

        # Reset stepDiscription value
        if globVal.stepDiscription != 'NA':
            globVal.stepDiscription = 'NA'
        # Report.saveHTMLReport()
    @staticmethod
    def customReport(StepDescription,ActualResult,ReportStatus):
        global htmlCollector
        htmlCollector = htmlCollector + '<tr><td></td><td>' + StepDescription + '</td><td>' + ActualResult + '</td>'

        if ReportStatus.lower() == 'passed':
            htmlCollector = htmlCollector +'<th style="color:#2EAF2E;text-align:center";>Passed</th><td style="text-align:center">' + Report.getCurrentTime() + '</td><td></td></tr>'
            globVal.totalPassed += 1
        elif ReportStatus.lower() == 'failed':
            if Report.takeScreenshot():
                absolutePath = os.path.abspath(globVal.testResultFolderPath + '/' + str(globVal.screenshotCount) + '.png')
                htmlCollector = htmlCollector +'<th style="color:#FF0000;text-align:center";>Failed</th><td style="text-align:center">' + Report.getCurrentTime() + '</td><td style="color:#FF0000;text-align:center"><a href ="' + str(absolutePath) + '" >' + str(globVal.screenshotCount) + '.png' + '</a></td></tr>'
            else:
                htmlCollector = htmlCollector +'<th style="color:#FF0000;text-align:center";>Failed</th><td style="text-align:center">' + Report.getCurrentTime() + '</td><td style="color:#FF0000;text-align:center">Screenshot Not Captured</td></tr>'
            globVal.totalFailed += 1
        elif ReportStatus.lower() == 'warning':
            htmlCollector = htmlCollector + '<th style="color:#8b2323;text-align:center";>Warning</th><td style="text-align:center">' + Report.getCurrentTime() + '</td><td></td></tr>'
            globVal.totalWarning += 1
        elif ReportStatus.lower() == 'information':
            htmlCollector = htmlCollector +'<td style="text-align:center";>Information</td><td style="text-align:center">' + Report.getCurrentTime() + '</td><td></td></tr>'
            globVal.totalInformation+=1
        else:
            htmlCollector = htmlCollector +'<th style="color:#FB0202;text-align:center";> Entered Invalid Status is" ' + ReportStatus +'"</th><td style="text-align:center">' + Report.getCurrentTime() + '</td><td></td></tr>'

        # Reset stepDiscription value
        if globVal.stepDiscription != 'NA':
            globVal.stepDiscription = 'NA'
        # Report.saveHTMLReport()
    @staticmethod
    def saveHTMLReport():
        global htmlCollector
        globVal.testEndTime = Report.getTestEndTime()
        FMT = "%d-%b-%y %I:%M:%S %p"
        globVal.testDuration = datetime.strptime(globVal.testEndTime, FMT) - datetime.strptime(globVal.testStartTime, FMT)
        htmlCollector = htmlCollector.replace('testEndTime',globVal.testEndTime)
        htmlCollector = htmlCollector.replace('testDuration',str(globVal.testDuration))
      # htmlCollector = htmlCollector.replace('browserName',str(globVal.testBrowser))
        htmlCollector = htmlCollector.replace('totalPassed',str(globVal.totalPassed))
        htmlCollector = htmlCollector.replace('totalFailed',str(globVal.totalFailed))
        htmlCollector = htmlCollector.replace('totalWarnings',str(globVal.totalWarning))
        htmlCollector = htmlCollector.replace('totalInformation',str(globVal.totalInformation))
        htmlCollector = htmlCollector.replace('totalSteps',str(globVal.totalSteps))
        htmlCollector = htmlCollector.replace('scriptCompletelyExecuted',str(globVal.scriptCompletelyExecuted))

        #hs = open("../Results/" + GlobalVariables.testCaseName + time.strftime("%Y%m%d-%H%M%S") + ".html", 'w')
        hs = open(globVal.testResultFolderPath + "/Results.html", 'w')
        hs.write(htmlCollector)
        hs.close()

