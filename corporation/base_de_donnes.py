import mysql.connector

def connection_Base():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='classicmodels',
            user='root',
            password='')

        if connection.is_connected():
            return connection
    except mysql.connector.errors as e:
        print("L'erreur de connection dans la base de donnees ", e)
        raise e
