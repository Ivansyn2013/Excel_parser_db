import openpyxl

book = openpyxl.open('files/sample.xlsm', read_only=False, keep_vba=True) #если открываем только на чтение

sheet = book.active

cells = sheet['A1':'W12']
print(cells[0])
print('***'*100)
print(cells[0][0])

for i in cells[6]:
    print (i.value)
