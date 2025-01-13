import psycopg2

rds_host = "kitchenaid-database-1.cdygoc0oc2f1.ap-southeast-2.rds.amazonaws.com"
port = "5432"
database = "kitchenaid-database-1"
user = "postgres"
pw = "2tXy3412!"

def get_DB_version():
    try:
        conn = psycopg2.connect(
            host=rds_host,
            port = port,
            database = database,
            user = user,
            password = pw
        )

        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        return (f"Datavase version: {version[0]}")
    except Exception as e:
        print(f"Error connection to the database: {e}")
        return ("Could not connect to DB")
    
def add_product(product):
    name = product.get("name")
    url = product.get("url")
    company = product.get("company")

    try:
        conn = psycopg2.connect(
            host=rds_host,
            port = port,
            database = database,
            user = user,
            password = pw
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
    
def get_products(product):
    name = product.get("name")
    url = product.get("url")
    company = product.get("company")

    try:
        conn = psycopg2.connect(
            host=rds_host,
            port = port,
            database = database,
            user = user,
            password = pw
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