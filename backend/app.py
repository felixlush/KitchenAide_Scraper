from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_cors import cross_origin
import psycopg2
from scraping import scrape_all_products, get_single_price
from database import get_db_products, add_product_db, get_db_companies

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")

@app.route("/api/scrape", methods=["GET"])
def scrape():
    products = get_db_products()
    # print(products)
    results = scrape_all_products(products)
    return jsonify(results), 200

@app.route("/api/scrape/single_price", methods=["GET"]) 
def scrape_single_price():
    results = get_single_price("https://www.kitchenwarehouse.com.au/product/kitchenaid-artisan-kek1701-electric-kettle-1-7l-matte-black", "Kitchen Warehouse")
    return jsonify(results, 200)

@app.route("/api/products", methods=["GET"])
def db_connect():
    try:
        return get_db_products()
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500
    
@app.route("/api/companies", methods=["GET"])
def get_companies():
    try:
        return get_db_companies()
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500

@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.json
    try:
        result = add_product_db(data)
        return jsonify({"message": result}), 201  # Return success message with 201 status code
    except psycopg2.IntegrityError as e:
        print(f"Integrity error: {e}")
        return jsonify({"error": "Integrity error, possibly duplicate entry"}), 400
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return jsonify({"error": "Database error"}), 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": "Unexpected error occurred"}), 500
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


