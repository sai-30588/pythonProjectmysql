import mysql.connector

try:
    # establishing the connection
    conn = mysql.connector.connect(user='root',
                                   password='m7842621830',
                                   host='127.0.0.1')

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Doping database DATABASE if already exists.
    cursor.execute("DROP database IF EXISTS s4")

    # Preparing query to create a database
    sql = "CREATE database S4"

    # Creating a database
    cursor.execute(sql)

    # Retrieving the list of databases
    print("List of databases: ")
    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())

except mysql.connector.Error as error:
    print("Failed to create database into MySQL table {}".format(error))
finally:
    if conn.is_connected():
        # Closing the connection
        cursor.close()
        conn.close()
        print("MySql Connection is closed")
