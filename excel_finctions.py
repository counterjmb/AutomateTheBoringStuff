import openpyxl
import os

workbook = openpyxl.load_workbook('example.xlsx')
#get all sheets
sheets = workbook.sheetnames
print(sheets)
#load sheet
sheet = workbook['Sheet1']
#get known cell value
print(sheet['B1'].value)

#rows and columns start at 1, not 0
for i in range(1,7):
    print(i, sheet.cell(row=i, column=2).value)