import mysql.connector

try:
    connection = mysql.connector.connect(user='root',
                                         password='m7842621830',
                                         host='127.0.0.1',
                                         database = 's4')

    mySql_select_query = 'select * from student'
    cursor = connection.cursor()
    cursor.execute(mySql_select_query)
    data = cursor.fetchall()
    for d in data:
        print(d)
    connection.commit()

except mysql.connector.Error as error:
    print("Failed to select record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")