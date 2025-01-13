from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_cors import cross_origin
from scraping import scrape_all_products, get_single_price

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

products = [
    {
        "Name": "ksm195 Porcelain White",
        "URL": "https://www.harveynorman.com.au/kitchenaid-artisan-stand-mixer-porcelain-white.html",
        "Price": "949",
        "Company": "Harvey Norman",
        "Timestamp": "13/01/2025"
    },
    {
        "Name": "ksm195 Onyx Black",
        "URL": "https://www.myer.com.au/p/kitchenaid-artisan-stand-mixer-in-onyx-black",
        "Price": "879",
        "Company": "Myer",
        "Timestamp": "13/01/2025"
    },
    {
        "Name": "ksm195 Matt Black",
        "URL": "https://www.thegoodguys.com.au/kitchenaid-artisan-stand-mixer-matt-black-5ksm195psabm",
        "Price": "899",
        "Company": "The Good Guys",
        "Timestamp": "13/01/2025"
    },
    {
        "Name": "ksm195 Matt Black",
        "URL": "https://www.jbhifi.com.au/products/kitchenaid-ksm195-4-7l-artisan-stand-mixer-matte-black",
        "Price": "899",
        "Company": "JB HI FI",
        "Timestamp": "13/01/2025"
    },
    {
        "Name": "ksm195 Pistachio",
        "URL": "https://www.davidjones.com/product/kitchenaid-ksm195-artisan-tilt-head-stand-mixer-25330462?nav=930836",
        "Price": "949",
        "Company": "David Jones",
        "Timestamp": "13/01/2025"
    },
    {
        "Name": "ksm195 Pistachio",
        "URL": "https://www.kitchenwarehouse.com.au/product/kitchenaid-artisan-ksm195-stand-mixer-pistachio",
        "Price": "699.95",
        "Company": "Kitchen Warehouse",
        "Timestamp": "13/01/2025"
    },
    {
        "Name": "ksm195 Porcelain White",
        "URL": "https://www.harveynorman.co.nz/home-appliances/kitchen-appliances/mixers/kitchenaid-ksm195-artisan-stand-mixer-porcelain-white.html",
        "Price": "999",
        "Company": "Harvey Norman NZ",
        "Timestamp": "13/01/2025"
    },
    {
        "Name": "ksm195 Empire Red",
        "URL": "https://www.stevens.co.nz/kitchenaid-artisan-ksm195-mixer-empire-red-6827512",
        "Price": "899.99",
        "Company": "Stevens NZ",
        "Timestamp": "13/01/2025"
    },
    {
        "Name": "EK1701 - Kettle Pistachio",
        "URL": "https://www.myer.com.au/p/kitchenaid-kettle-17l-in-pistachio-5kek1701apt",
        "Price": "PLACEHOLDER",
        "Company": "Myer",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "EK1701 - Kettle Almond",
        "URL": "https://www.jbhifi.com.au/products/kitchenaid-kek170-1-7l-variable-temperature-electric-kettle-almond",
        "Price": "PLACEHOLDER",
        "Company": "JB HI FI",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "EK1701 - Kettle Almond Cream",
        "URL": "https://www.thegoodguys.com.au/kitchenaid-17l-almond-cream-kettle-5kek1701aac",
        "Price": "PLACEHOLDER",
        "Company": "The Good Guys",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "EK1701 - Kettle Variable Temperature",
        "URL": "https://www.davidjones.com/product/kitchenaid-kek1701apl-17l-variable-temperature-kettle-27031587",
        "Price": "PLACEHOLDER",
        "Company": "David Jones",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "EK1701 - Kettle Matte Black",
        "URL": "https://www.kitchenwarehouse.com.au/product/kitchenaid-artisan-kek1701-electric-kettle-1-7l-matte-black",
        "Price": "PLACEHOLDER",
        "Company": "Kitchen Warehouse",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT2109 - 2 Slice Toaster Almond Cream",
        "URL": "https://www.myer.com.au/p/kitchenaid-2-slice-toaster-in-almond-cream-5kmt2109aac",
        "Price": "PLACEHOLDER",
        "Company": "Myer",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT2109 - 4 Slice Toaster Porcelain White",
        "URL": "https://www.myer.com.au/p/kitchenaid-toaster-4-slice-kmt4109-in-porcelain-white",
        "Price": "PLACEHOLDER",
        "Company": "Myer",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT2109 - 2 Slice Toaster Almond Cream",
        "URL": "https://www.harveynorman.com.au/kitchenaid-2-slice-toaster-almond-cream.html",
        "Price": "PLACEHOLDER",
        "Company": "Harvey Norman",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT2109 - 2 Slice Toaster Matte Black",
        "URL": "https://www.thegoodguys.com.au/kitchenaid-2-slice-toaster-matte-black-5kmt2109abm",
        "Price": "PLACEHOLDER",
        "Company": "The Good Guys",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT2109 - 2 Slice Toaster",
        "URL": "https://www.davidjones.com/product/kitchenaid-kmt2109apl-2-slice-toaster-27031583",
        "Price": "PLACEHOLDER",
        "Company": "David Jones",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT2109 - 2 Slice Toaster Black Matte",
        "URL": "https://www.kitchenwarehouse.com.au/product/kitchenaid-artisan-kmt2109-2-slice-toaster-black-matte",
        "Price": "PLACEHOLDER",
        "Company": "Kitchen Warehouse",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT2109 - 2 Slice Toaster Cast Iron",
        "URL": "https://www.jbhifi.com.au/products/kitchenaid-kmt2109-2-slice-toaster-cast-iron",
        "Price": "PLACEHOLDER",
        "Company": "JB HI FI",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT4109 - 4 Slice Toaster Porcelain White",
        "URL": "https://www.harveynorman.com.au/kitchenaid-4-slice-toaster-porcelain-white.html",
        "Price": "PLACEHOLDER",
        "Company": "Harvey Norman",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT4109 - 4 Slice Toaster Porcelain White",
        "URL": "https://www.myer.com.au/p/kitchenaid-toaster-4-slice-kmt4109-in-porcelain-white",
        "Price": "PLACEHOLDER",
        "Company": "Myer",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT4109 - 4 Slice Toaster Stainless Steel",
        "URL": "https://www.thegoodguys.com.au/kitchenaid-4-slice-toaster-stainless-steel-5kmt4109asx",
        "Price": "PLACEHOLDER",
        "Company": "The Good Guys",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT4109 - 4 Slice Toaster",
        "URL": "https://www.davidjones.com/product/kitchenaid-kmt4109apl-4-slice-toaster-27031585",
        "Price": "PLACEHOLDER",
        "Company": "David Jones",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT4109 - 4 Slice Toaster Empire Red",
        "URL": "https://www.kitchenwarehouse.com.au/product/kitchenaid-artisan-kmt4109-4-slice-toaster-empire-red",
        "Price": "PLACEHOLDER",
        "Company": "Kitchen Warehouse",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KMT4109 - 4 Slice Toaster Matte Black",
        "URL": "https://www.jbhifi.com.au/products/kitchenaid-kmt4109-4-slice-toaster-matte-black",
        "Price": "PLACEHOLDER",
        "Company": "JB HI FI",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KSB4027 - K400 Blender Dried Rose",
        "URL": "https://www.myer.com.au/p/kitchenaid-k400-variable-sped-blender-dried-rose-5ksb4027adr",
        "Price": "PLACEHOLDER",
        "Company": "Myer",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KSB4027 - K400 Blender Contour Silver",
        "URL": "https://www.jbhifi.com.au/products/kitchenaid-ksb4027-variable-speed-blender-contour-silver",
        "Price": "PLACEHOLDER",
        "Company": "JB HI FI",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KSB4027 - K400 Blender",
        "URL": "https://www.davidjones.com/product/kitchenaid-k400-blender-23691973",
        "Price": "PLACEHOLDER",
        "Company": "David Jones",
        "Timestamp": "PLACEHOLDER"
    },
    {
        "Name": "KSB4027 - K400 Blender Empire Red",
        "URL": "https://www.kitchenwarehouse.com.au/product/kitchenaid-k400-variable-speed-blender-1-7l-empire-red",
        "Price": "PLACEHOLDER",
        "Company": "Kitchen Warehouse",
        "Timestamp": "PLACEHOLDER"
    }
]


@app.route("/")

def hello_world():
    return "Hello From Flash Backend!"

@app.route("/api/hello")
def hello_api():
    return jsonify({"message": "Hello from the flash api!"})

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/api/products", methods=["POST"])
def add_products():
    data = request.json
    products.append(data)
    return jsonify({"message": "product added successfully"}), 201

@app.route("/api/scrape", methods=["GET"])
def scrape():
    results = scrape_all_products(products)
    return jsonify(results), 200

@app.route("/api/scrape/single_price", methods=["GET"]) 
def scrape_single_price():
    results = get_single_price("https://www.harveynorman.com.au/kitchenaid-artisan-stand-mixer-porcelain-white.html", "Harvey Norman")
    return jsonify(results, 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


