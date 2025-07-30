import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

def get_DB_version():
    try:
        conn  = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )

        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        return (f"Datavase version: {version[0]}")
    except Exception as e:
        print(f"Error connection to the database: {e}")
        return ("Could not connect to DB")
    
def add_product_db(product):
    name = product.get("name")
    url = product.get("url")
    company = product.get("company")
    sku = product.get("sku")
    colour = product.get("colour")

    try:
        conn  = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )

        cursor = conn.cursor()
        SQL = "INSERT INTO products (name, url, company, sku, colour) VALUES (%s, %s, %s, %s, %s)"
        data = (name, url, company, sku, colour)
        cursor.execute(SQL, data)
        conn.commit()
        print(f"Product added successfully")
        return(f"Product added successfully") 

    except psycopg2.IntegrityError as e:
            print(f"Integrity error: {e}")
            conn.rollback()  # Rollback the transaction on integrity error
            return "Failed to add product: Integrity error"

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        conn.rollback()  # Rollback the transaction on general database error
        return "Failed to add product: Database error"

    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Failed to add product: Unexpected error"
    
    finally:
        if conn:
            conn.close()

def update_db_product(product):
    id = product.get("id")
    name = product.get("name")
    url = product.get("url")
    company = product.get("company")
    sku = product.get("sku")
    colour = product.get("colour")
    print(f"Updating product with ID: {id}, Name: {name}, URL: {url}, Company: {company}, SKU: {sku}, Colour: {colour}")

    try:
        conn  = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )

        cursor = conn.cursor()
        SQL = "UPDATE products SET name = %s, url = %s, company = %s, sku = %s, colour = %s WHERE id = %s"
        data = (name, url, company, sku, colour, id)
        cursor.execute(SQL, data)
        if cursor.rowcount == 0:
            print("No rows were updated. Check if the product ID exists.")
        else:
            print(f"Product updated successfully. {cursor.rowcount} row(s) affected.")
        conn.commit()
    
    except psycopg2.IntegrityError as e:
            print(f"Integrity error: {e}")
            conn.rollback()  # Rollback the transaction on integrity error
            return "Failed to update product: Integrity error"

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        conn.rollback()  # Rollback the transaction on general database error
        return "Failed to update product: Database error"

    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Failed to update product: Unexpected error"
    
    finally:
        if conn:
            conn.close()

def get_db_products(search_term, filter_term):
    try:
        conn = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )
        cursor = conn.cursor()

        SQL = "SELECT id, name, url, company, sku, colour FROM products WHERE 1=1"  # 1=1 makes it easy to append conditions
        params = []

        if search_term:
            SQL += " AND (LOWER(name) ILIKE %s OR LOWER(sku) ILIKE %s)"
            params.extend([f"%{search_term}%", f"%{search_term}%"])

        if filter_term:
            SQL += " AND LOWER(company) ILIKE %s"
            params.append(f"%{filter_term}%")

        cursor.execute(SQL, tuple(params))

        products = cursor.fetchall()
        result = [
            {"id": row[0], "name": row[1], "url": row[2], "company": row[3], "sku": row[4], "colour": row[5]}
            for row in products
        ]
        
        return result

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return "Failed to get products: Unexpected error"

    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Failed to add products: Unexpected error"
    
def get_db_companies():
    try:
        conn  = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )

        cursor = conn.cursor()
        SQL = "SELECT company_id, company_name FROM companies"
        cursor.execute(SQL)

        rows = cursor.fetchall()

        products = [
            {
                "id": row[0],
                "name": row[1]
            }
            for row in rows
        ]

        return products

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        conn.rollback()  # Rollback the transaction on general database error
        return "Failed to get companies: Database error"

    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Failed to get companies: Unexpected error"