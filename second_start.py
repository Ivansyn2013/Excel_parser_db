import openpyxl

book = openpyxl.open('files/sample.xlsm', read_only=True) #если открываем только на чтение

sheet = book.active

#указание ячеек по индесам первый столбец второй строка.
#причем нулевого столбца нет, начало с первого
# sheet.max_row получить количество строк листа

cells = sheet['A2':"W12"]
tmp = []

FIRST_ROW = sheet['A2':'W2']
#print(FIRST_ROW[0])
for i in FIRST_ROW[0]:
    tmp.append(i.value)

RESULT = tmp[1:12] + tmp [13:]
# print(RESULT)
# print(len(RESULT))
# for i in cells:
#     for x in i:
#         print(x.value)
#
#
#
# print(sheet[1][0].value)