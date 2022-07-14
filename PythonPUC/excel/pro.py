import openpyxl as xl
a=xl.load_workbook('null.xlsx')
sheet=a['Sheet1']
b=sheet['a1']
b1=sheet.cell(1,2)
print(b)
print(b.value)
