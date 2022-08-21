import mysql.connector
import pandas as pd
import numpy as np
from mysql.connector import connect, Error
from getpass import getpass


data = pd.read_excel('./ex_data.xlsm')
take_data = np.where(data['Производитель'].str.startswith('Терумо'),
                     data['Производитель'],
                     np.nan)

take_d_list = [ (str(x),) for x in take_data]
print (take_d_list)


try:
    with connect(
        host='localhost',
        port='3333',
        user='user1',
        password='123',
        database='med_product',
    ) as connection:

        #print(connection)

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

        insert_protucts_qurey = '''
            INSERT INTO product
            (name)
            VALUES( %s)
        '''



        with connection.cursor() as cursor:
            cursor.execute(show_db)
            for db in cursor:
                print(db)

            cursor.execute(show_tables)
            for res in cursor:
                print('Tables '+ res[0])


            # cursor.execute(create_tb)
            # connection.commit()

            cursor.executemany(insert_protucts_qurey, take_d_list)
            connection.commit()

except Error as e:
    print('this is a error', e)
