import pymysql

def connect():
    return pymysql.connect(host="localhost", user="root", password="", database="dbitems",
                            cursorclass=pymysql.cursors.DictCursor)

def fetch_all_items():
    connection=connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM items")
            rows = cursor.fetchall()
        return rows
    finally:
        connection.close()

def insert_item(name, description):
    connection=connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO items (name, description) VALUE (%s, %s)", (name,description))
            connection.commit()
        return 1
    finally:
        connection.close()

def fetch_item_by_id(item_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM items WHERE id = %s", (item_id))
            rows = cursor.fetchone()
        return rows
    finally:
        connection.close()

def update_item(item_id, name, description):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE items SET name = %s, description = %s WHERE id = %s",(name, description, item_id)),
            connection.commit()
        return 1
    finally:
        connection.close()

def delete_item(item_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM items WHERE id = %s",(item_id))
            connection.commit()
        return 1
    finally:
        connection.close()