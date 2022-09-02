import time
from collections import OrderedDict

from mysql.connector import connect, Error


#
# try:
#     with connect(
#         host='192.168.0.110',
#         port='3306',                        #может принимать объект в виде словаря
#         user='user1',
#         password='123',
#         database='med_product_db',
#     ) as connection:
#
#         print('Connecting-', connection)
#         #print(dir(connection))
#
#         with connection.cursor() as cursor:
#             # cursor.execute('DESCRIBE introducer;')
#             cursor.execute('SELECT `dfdf` from maker')
#
#             for i in cursor:
#                 print(i[0])
#
#
# except Error as e:
#     print('this is a error', e)
#     print(e.errno)


def get_fields(db_name, table_name):
    '''connecting to db, takes fields from table and return tuple of them'''
    result = []
    try:
        with connect(
                host='192.168.0.110',
                port='3306',  # может принимать объект в виде словаря
                user='user1',
                password='123',
                database=db_name,
        ) as connection:
            with connection.cursor(buffered=True) as cursor:
                exec_str = 'DESCRIBE {};'.format(table_name)
                cursor.execute(exec_str)
                for i in cursor:
                    result.append(i[0])

        return tuple(result)

    except Error as e:
        return ('this is an error', e)


def sql_intro_req(table_name, fields, maker_name):
    '''take  fields, return srt with sql req format key : val - filed : values %s'''

    placeholders = ", ".join(["%s"] * (len(fields[1:])))

    # set_and_push = ''''INSERT INTO {}(maker_id) SELECT id FROM maker WHERE maker_name = {}'''.format(table_name,
    #                                                                                                  maker_name)

    sql = "INSERT INTO {} {} SELECT id, {} FROM maker WHERE maker_name = '{}'".format(table_name,
                                                                                      str(fields).replace("'", ''),
                                                                                      placeholders, maker_name)
    # print(sql)
    return sql

# print(get_fields('med_product_db','introducer'))
# tmp = get_fields('med_product_db','introducer' )
# print(sql_intro_req('introducer', tmp[2:]))
