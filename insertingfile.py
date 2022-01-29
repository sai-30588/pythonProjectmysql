import mysql.connector

try:
    connection = mysql.connector.connect(user='root',
                                         password='m7842621830',
                                         host='127.0.0.1',
                                         database = 's4')

    mySql_insert_query = """INSERT INTO STUDENT (stuid, stuname, sub1, sub2,sub3) 
                           VALUES (%s, %s, %s, %s, %s) """

    records_to_insert = [(3214, 'Jhanvi', 79, 80, 65),
                         (3245, 'Prakash', 89, 70, 75),
                         (3268, 'Jhanvi', 70, 87, 85)]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into student table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")