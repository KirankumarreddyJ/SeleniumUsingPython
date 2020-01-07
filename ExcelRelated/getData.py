# import openpyxl,sys
#
# def getDataFromDataSheet(file_path, sheet_name, data_column_name, script_name):
#     try:
#         wb = openpyxl.load_workbook(filename=file_path,read_only=True)
#         sh = wb[sheet_name]
#
#         maxRow = sh.max_row
#         maxColumn = sh.max_column
#         reqRowNum = 1
#         reqColumNum = 1
#         for r in range(1,maxRow+1):
#             if str(sh.cell(r,1).value).lower() == str(script_name).lower():
#                 reqRowNum = r
#                 break
#             else:
#                 if r == maxRow:
#                     print('"'+str(script_name) + '" is not found in given sheet name "' + str(sheet_name)+'"')
#                     return False
#         for c in range(1, maxColumn + 1):
#             if str(sh.cell(1, c).value).lower() == str(data_column_name).lower():
#                 reqColumNum = c
#                 break
#             else:
#                 if c == maxColumn:
#                     print('"'+str(data_column_name) + '" is not found in given sheet name "' + str(sheet_name)+'"')
#                     return False
#         requiredData = sh.cell(reqRowNum,reqColumNum).value
#         return requiredData
#     except Exception as e:
#         print('Data not retrived',e)
#         return False
#     finally:
#         wb._archive.close()
# dataFromExcel = getDataFromDataSheet("../TestData/TestData.xlsx",'TestData','emailId','test_001_registration')
# print(dataFromExcel)