from corporation import base_de_donnes



def recuperation_produit():
    try:
        connection = base_de_donnes.connection_Base()
        cursor = connection.cursor()
        sql_select_Query = """SELECT productCode,productName,MSRP  from products  order by quantityInStock desc limit 5"""
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.close()
        return records
    except Exception as e:
        print("error reading data from mysql table", e)
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


def recuperation_categories():
    try:
        connection = base_de_donnes.connection_Base()
        cursor = connection.cursor()
        sql_select_Query = """SELECT productLine, textDescription FROM productlines"""
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cursor.close()
        return records
    except Exception as e:
        print("error reading data from mysql table", e)
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
