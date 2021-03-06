from flask import Flask

app = Flask(__name__)

@app.route('/product')
def get_all_products():
    return {'stub':'will contain all products'}, 200

# Intentionally not using `<int:productId>` here to control the HTTP status code returned
@app.route('/product/<productId>')
def get_product(productId):
    return {'stub':'get product {}'.format(productId)}, 200

@app.route('/store/inventory')
def get_inventory():
    return {'stub':'inventory'}, 200

if __name__ == '__main__':
    app.run()