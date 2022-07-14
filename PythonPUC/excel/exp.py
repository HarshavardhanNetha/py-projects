import openpyxl as xl
a=xl.load_workbook('null.xlsx')
sheet=a['Sheet']
a1=[]
for i in range(1,7):
    b=sheet['a{}'.format(i)]
    a1.append(b.value)
print(a1)
y=[]
while(1):
    x=int(input('Search:'))
    if(x in a1):
        print('Registered')
        
        if(x not in y):
            print('You can go in.')
            y.append(x)
        else:
            print('Already in AUdit...')
    else:
        print('Not reg.')
