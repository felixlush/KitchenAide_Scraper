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

    try:
        conn  = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )

        cursor = conn.cursor()
        SQL = "INSERT INTO products (name, url, company) VALUES (%s, %s, %s)"
        data = (name, url, company)
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
    
def get_db_products():
    try:
        conn  = psycopg2.connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            port=PORT,
            dbname=DBNAME
        )

        cursor = conn.cursor()
        SQL = "SELECT * FROM products"
        cursor.execute(SQL)

        rows = cursor.fetchall()

        products = [
            {
                "id": row[0],
                "name": row[1],
                "url": row[2],
                "company": row[3]
            }
            for row in rows
        ]

        return products

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        conn.rollback()  # Rollback the transaction on general database error
        return "Failed to add product: Database error"

    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Failed to add product: Unexpected error"
    
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