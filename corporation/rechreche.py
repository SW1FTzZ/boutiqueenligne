import mysql.connector


def cherche_employe(keyword, page=1):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='classicmodels',
            user='root',
            password='')

        if connection.is_connected():
            item_per_page = 10
            offset = (page - 1) * item_per_page
            sql_select_Query = """SELECT productCode, productName, MSRP, productDescription from products where productName like %s limit %s,%s"""

            cursor = connection.cursor()
            params = ('%{}%'.format(keyword), offset, item_per_page,)
            cursor.execute(sql_select_Query, params)

            records = cursor.fetchall()
            print("Total number of rows in table", cursor.rowcount)
            return records

    except mysql.connector.Error as e:
        print("Error connection database", e)
        raise e
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
