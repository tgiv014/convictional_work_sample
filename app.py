from flask import Flask, jsonify
import re
from product import ProductCollection
import schemas

product_collection = ProductCollection()

app = Flask(__name__)


@app.route('/product')
def get_all_products():
    products = product_collection.get_all()
    filled_product_schemas = [schemas.map_product_schema(
        product) for product in products]
    return jsonify(filled_product_schemas), 200

# Intentionally not using `<int:productId>` here to control the HTTP status code returned


@app.route('/product/<productId>')
def get_product(productId):
    if re.match(r'[0-9]+', productId) is None:
        return "Invalid ID supplied", 400

    product = product_collection.get(int(productId))

    if product is None:
        return "product not found", 404
    # Early return checks are good, let's fill out a product schema

    filled_product_schema = schemas.map_product_schema(product)

    return jsonify(filled_product_schema), 200


@app.route('/store/inventory')
def get_inventory():
    products = product_collection.get_all()
    inventory = schemas.map_inventory_schema(products)
    return jsonify(inventory), 200


if __name__ == '__main__':
    app.run()
