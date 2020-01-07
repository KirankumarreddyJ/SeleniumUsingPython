from selenium.webdriver import Chrome
from FunctionLibrery.globalFunctionLibrery import GlobalFunction
from FunctionLibrery.htmlFunctionLibrery import Report
from FunctionLibrery.constantLibrery import ConstantLibrery as cnsLib

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
driver = Chrome(executable_path = "..\Drivers\chromedriver.exe")
driver.implicitly_wait(20)
driver.maximize_window()

driver.get('https://chercher.tech/python/table-selenium-python#')

w = driver.find_element_by_xpath("//body[@id='page-top'][1]")

print(w.get_property("id"))
print(w.get_property("class"))

print(w.get_attribute("id"))
print(w.get_attribute("class"))

rows = len(w.find_elements_by_xpath("//tr"))
cols = len(w.find_elements_by_xpath("//tr[2]/td"))

print("Rows", rows)
print("Columns", cols)

allData = []
for r in range(1,rows+1):
    rowData = []
    for c in range(1,cols+1):
        if r ==1:
            rowData.append(w.find_element_by_xpath("//tr[" + str(r) + "]/th[" + str(c) + "]").text)
        else:
            rowData.append(w.find_element_by_xpath("//tr["+str(r)+"]/td["+str(c)+"]").text)

    allData.append(rowData)

print(allData)

def getCellDataFromWebTable(webTableObject,rowNumber,columnNumber,expResult,unExpResult, stepName, testStatus):
    try:
        if str(stepName).lower() == 'stepname':
            stepName = 'Get cellData in row ' + str(rowNumber) +' & column ' + str(columnNumber) +' from "' + str(cnsLib.getObjDescription(webTableObject)) + '"'

        #check rowNumber & columnNumber contains int value
        int(rowNumber);int(columnNumber)

        tableObj = GlobalFunction.getDriverObjForWebObj(webTableObject)
        cellData = str(tableObj.find_element_by_xpath("//tr[" + str(rowNumber) + "]/td[" + str(columnNumber) + "]").text)
        Report.customReport(stepName, str(cellData) + ' is retrived for Web Table', expResult)
        return cellData
    except Exception as e:
        Report.customReport(stepName, 'Cell data not found. Error is : "' + str(e) + '"', unExpResult)
        GlobalFunction.exitTest(testStatus)
        return False

def getRowCountFromWebTable(webTableObject,expResult,unExpResult, stepName, testStatus):
    try:
        if str(stepName).lower() == 'stepname':
            stepName = 'Get Row count of WebTable <' + str(cnsLib.getObjDescription(webTableObject)) + '>'

        tableObj = GlobalFunction.getDriverObjForWebObj(webTableObject)
        rows = len(tableObj.find_elements_by_xpath("//tr"))
        Report.customReport(stepName, 'Row count (' + str(rows) + ') is retrived from Web Table', expResult)
        return rows
    except Exception as e:
        Report.customReport(stepName, 'Row count not retrived. Error is : "<' + str(e) + '>"', unExpResult)
        GlobalFunction.exitTest(testStatus)
        return False

def getColumnCountFromWebTable(webTableObject, expResult, unExpResult, stepName, testStatus):
    try:
        if str(stepName).lower() == 'stepname':
            stepName = 'Get Column count of WebTable <' + str(cnsLib.getObjDescription(webTableObject)) + '>'

        tableObj = GlobalFunction.getDriverObjForWebObj(webTableObject)
        cols = len(tableObj.find_elements_by_xpath("//tr[1]/th"))
        Report.customReport(stepName, 'Column count (' + str(cols) + ') is retrived from Web Table', expResult)
        return cols
    except Exception as e:
        Report.customReport(stepName, 'Column count not retrived. Error is : "<' + str(e) + '>"', unExpResult)
        GlobalFunction.exitTest(testStatus)
        return False

def getTotalDataFromWebTable(webTableObject, expResult, unExpResult, stepName, testStatus):
    try:
        if str(stepName).lower() == 'stepname':
            stepName = 'Get Total Data from WebTable <' + str(cnsLib.getObjDescription(webTableObject)) + '>'

        tableObj = GlobalFunction.getDriverObjForWebObj(webTableObject)
        rows = len(tableObj.find_elements_by_xpath("//tr"))
        cols = len(tableObj.find_elements_by_xpath("//tr[1]/th"))

        allData = []
        for r in range(1, rows + 1):
            rowData = []
            for c in range(1, cols + 1):
                if r == 1:
                    rowData.append(tableObj.find_element_by_xpath("//tr[" + str(r) + "]/th[" + str(c) + "]").text)
                else:
                    rowData.append(tableObj.find_element_by_xpath("//tr[" + str(r) + "]/td[" + str(c) + "]").text)
            allData.append(rowData)
        Report.customReport(stepName, 'Total Data is retrived from WebTable', expResult)
        return allData

    except Exception as e:
        Report.customReport(stepName, 'Total Data is not retrived from WebTable. Error is : "<' + str(e) + '>"', unExpResult)
        GlobalFunction.exitTest(testStatus)
        return False


def getWebObjectAttributeValue(webObject,attributeName, expResult, unExpResult, stepName, testStatus,waitTime):
    try:
        if str(stepName).lower() == 'stepname':
            stepName = 'Get Attribute(' + str(attributeName) +') value from <' + str(cnsLib.getObjDescription(webObject)) + '>'

        obj = GlobalFunction.getDriverObjForWebObj(webObject)
        value = w.get_attribute(str(attributeName))
        Report.customReport(stepName, "Value retrived from <'" + str(cnsLib.getObjDescription(webObject)) + ">", expResult)
        return value

    except Exception as e:
        Report.customReport(stepName, "Value not retrived from <" + str(cnsLib.getObjDescription(webObject)) + ">. Error is : <" + str(e) + ">", unExpResult)
        GlobalFunction.exitTest(testStatus)
        return False


@staticmethod
def VerifyWebObjectEnabled(webObject, expResult, unExpResult, stepName, testStatus, waitTime):
    try:
        if str(stepName).lower() == 'stepname':
            stepName = 'Verify <' + str(cnsLib.getObjDescription(webObject)) + '> is Enabled'

        obj = GlobalFunction.getDriverObjForWebObj(webObject)
        result = obj.is_enabled()
        Report.customReport(stepName, '<' + str(cnsLib.getObjDescription(webObject)) + '> is Enabled', expResult)
        return result

    except Exception as e:
        Report.customReport(stepName, '<' + str(cnsLib.getObjDescription(webObject)) + '> is not Enabled. Error is : <' + str(e) + '>', unExpResult)
        GlobalFunction.exitTest(testStatus)
        return False

@staticmethod
def VerifyWebObjectSelected(webObject, expResult, unExpResult, stepName, testStatus, waitTime):
    try:
        if str(stepName).lower() == 'stepname':
            stepName = 'Verify <' + str(cnsLib.getObjDescription(webObject)) + '> is Selected'

        obj = GlobalFunction.getDriverObjForWebObj(webObject)
        result = obj.is_selected()
        Report.customReport(stepName, '<' + str(cnsLib.getObjDescription(webObject)) + '> is Selected', expResult)
        return result

    except Exception as e:
        Report.customReport(stepName, '<' + str(cnsLib.getObjDescription(webObject)) + '> is not Selected. Error is : <' + str(e) + '>', unExpResult)
        GlobalFunction.exitTest(testStatus)
        return False