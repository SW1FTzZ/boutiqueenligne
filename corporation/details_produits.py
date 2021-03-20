from corporation import base_de_donnes

def description_produit(productid):
    state = {
        "valid": True,
        "message": "",
        "produit": {},
    }
    try:
        connection = base_de_donnes.connection_Base()
        if connection.is_connected():
            sql_select_Query = """SELECT productCode, productLine, productName, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP from products WHERE productCode = %s"""
            cursor = connection.cursor(dictionary=True)
            params = (productid,)
            cursor.execute(sql_select_Query, params)
            records = cursor.fetchall()
            cursor.close()
            if len(records) != 1:
                state["valid"] = False
                state["message"] = f"Aucun enregistrement valide trouvé avec le nom {productid}"
            else:
                state["valid"] = True
                state["produit"] = records[0]
    except Exception as e:
        state["valid"] = False
        state["message"] = f"Error reading data from Mysql table {e}"
    return state


def description_produit_line(ligne):
    state = {
        "valid": True,
        "message": "",
        "produit": {},
    }
    try:
        connection = base_de_donnes.connection_Base()
        if connection.is_connected():
            sql_select_Query = """SELECT products.productLine, products.productName, productlines.textDescription FROM products INNER JOIN productlines ON products.productLine = productlines.productLine WHERE productlines.productLine = %s """
            cursor = connection.cursor(dictionary=True)
            params = (ligne,)
            cursor.execute(sql_select_Query, params)
            records = cursor.fetchall()
            cursor.close()
            if len(records) != 1:
                state["valid"] = False
                state["message"] = f"Aucun enregistrement valide trouvé avec le categorie {ligne}"
            else:
                state["valid"] = True
                state["produit"] = records[0]
    except Exception as e:
        state["valid"] = False
        state["message"] = f"Error reading data from Mysql table {e}"
    return state
