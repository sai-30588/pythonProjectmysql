import mysql.connector as mysql_conn

try:
    con_db = mysql_conn.connect(user='root',
                                password='m7842621830',
                                host='127.0.0.1',
                                database = 's4')

    con_cur  = con_db.cursor()

    sql_table = 'CREATE TABLE STUDENT(stuid int primary key,stuname varchar(20),' \
            'sub1 int, sub2 int, sub3 int)'

    con_cur.execute(sql_table)
    print("Table created Successfully")
    con_db.commit()
except mysql_conn.Error as error :
    print("Failed to Create table into MySQL table {}".format(error))

finally:
    if con_db.is_connected():
        con_cur.close()
        con_db.close()
        print("MySQL connection is closed")