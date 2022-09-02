import openpyxl
from collections import OrderedDict

book = openpyxl.open('files/sample.xlsm', read_only=True)  # если открываем только на чтение

sheet = book.active
# print(sheet.max_row)

makers = []
for i in sheet['A1':'A765']:
    makers.append(i[0].value)

makers_dict = dict.fromkeys(makers, [])


# makers.append(i.values)
# #указание ячеек по индесам первый столбец второй строка.
# #причем нулевого столбца нет, начало с первого
# # sheet.max_row получить количество строк листа
#
# cells = sheet['A2':"W12"]
# tmp = []
# COLLUM_NAMES = [ x.value for x in sheet['A1':'W1'][0]]
# FIRST_ROW = sheet['A2':'W2']
# #print(FIRST_ROW[0])
# for i in FIRST_ROW[0]:
#     tmp.append(i.value)
#
# RESULT = tmp[1:12] + tmp [13:]
# print(COLLUM_NAMES)
# print(RESULT)


# print(len(RESULT))
# for i in cells:
#     for x in i:
#         print(x.value)
#
#
#
# print(sheet[1][0].value)

def get_values_from_ex(num_row):
    '''take vakues of cells from excel file return it in OrderDict'''

    book = openpyxl.open('files/sample.xlsm', read_only=False, keep_vba=True)  # если открываем только на чтение
    sheet = book.active
    start = f'A{num_row}'
    finish = f'W{num_row}'
    COLLUM_NAMES = [x.value for x in sheet['A1':'W1'][0]]  # 0 потому что это срез, а я беру срез в одну строку
    cells_values = [x.value for x in sheet[start:finish][0]]
    result = dict(zip(COLLUM_NAMES, cells_values))
    # result = OrderedDict(zip(COLLUM_NAMES,cells_values))
    return result


# print(get_values_from_ex(2))
# print(get_values_from_ex(765)['Производитель'])
# tmp = [x for x in get_values_from_ex(2).values()]
# print(tmp)


dd = [(x,) for x in makers_dict.keys()]
# print(dd)
