from db_requsts import get_fields, sql_intro_req
from second_start import get_values_from_ex, dd
from mysql.connector import connect, Error
from getpass import getpass
#from second_start import FIRST_ROW
import second_start

#data = pd.read_excel('./ex_data.xlsm')
# take_data = np.where(data['Производитель'].str.startswith('Терумо'),
#                      data['Производитель'],
#                      np.nan)

#take_d_list = [ (str(x),) for x in take_data]
#print (take_d_list)


show_db = 'SHOW DATABASES'
show_tables = 'SHOW TABLES'
create_tb = ''' DROP TABLES IF EXISTS product;
                CREATE TABLE product ( 
                id  INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100),
                size VARCHAR (10),
                maker_name VARCHAR (100)
            )
            '''

insert_maker_name =\
    '''
    INSERT INTO maker
    (maker_name)
    VALUES( %s)
    '''
insert_intro_values = \
    '''
    INSERT INTO maker
    ( 'introducer_type', 'introducer_articul', 'introducer_length', 'introducer_size', 'gemostatic_valve', 
    'color_marker_of_size', 'side_valve', 'three_way_tap', 'fabric_iteam', 'dilatationv', 'obturation', 
    'micro_wire_length', 'mirco_wire_diameter', 'mirco_wire_tip_shape',  'spine_diametr', 'spine_length', 
    'surrenge_volume', 'dievice_for_wire_input', 'input_place',  'link_text', 'image')
    VALUES( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)
    '''
makers = set()
intro_collum_names = []

try:
    with connect(
        host='localhost',
        port='3333',
        user='user1',
        password='123',
        database='med_product_db',
    ) as connection:
        connection.autocommit=False
        print('Connecting-', connection.is_connected())

        with connection.cursor() as cursor:
            fields = get_fields('med_product_db','introducer')[3:]
            for i in range (2,50):
                values = tuple(x for x in get_values_from_ex(i).values())
                print(fields)
                print(values[1:])
                #print(str(fields).replace("'",''))
                req = sql_intro_req('introducer', fields, values[0])
                #print(values[1:])
                #print(dd)

                #cursor.executemany('INSERT INTO `maker`(`maker_name`) VALUES (%s)', dd[1:]) #заполнениие производителей
                # работает!
                print(req)
                cursor.execute(req, values[1:])
                print("Record Updated successfully ")
                print(i)
                print('*'*10)

            connection.commit()
            cursor.close()
        #connection.commit()


except Error as e:
    print('this is a error', e)
    #connection.rollback()
finally:
    # closing database connection.
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("connection is closed")


# try:
#     with connect(
#         host='192.168.0.110',
#         port='3306',
#         user='user1',
#         password='123',
#         database='med_product_db',
#     ) as connection:
#
#         print('Connecting-', connection)
#
#
#         with connection.cursor() as cursor:
#             #показать базы данных
#             # cursor.execute(show_db)
#             # for db in cursor:
#             #     print(db)
#             #показать таблицы бд
#             # cursor.execute(show_tables)
#             # for res in cursor:
#             #     print('Tables '+ res[0])
#
#
#             cursor.execute('DESCRIBE introducer;')
#             for i in cursor:
#                 intro_collum_names.append(i[0])
#             print(intro_collum_names)
#             # cursor.execute(create_tb)
#             # connection.commit()
#
#             #cursor.executemany(insert_protucts_qurey, take_d_list) (сначала куда, потом кого
#
#             #заполнение название производителя
#             cursor.execute(insert_maker_name, maker_name)
#
#             #заполнение полей
#             cursor.execute(insert_intro_values, intro_values)
#
#             connection.commit()
#             connection.close
# except Error as e:
#     print('this is a error', e)
