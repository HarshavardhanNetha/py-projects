import openpyxl as xl
a=xl.load_workbook('null.xlsx')
sheet=a['Sheet']
for i in range(1,sheet.max_row+1):
    b=sheet['a{}'.format(i)]
    print(b.value)
    update=input('New value;')
    sheet["b{}".format(i)]=update
a.save('new.xlsx')
