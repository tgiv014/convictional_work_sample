import requests

class ProductCollection:
    def __init__(self):
        # Initialize in-memory collection with the sample JSON
        r = requests.get('https://my-json-server.typicode.com/convictional/engineering-interview/products')
        
        # Store in a hashmap/dict for fast lookups by ID
        self.collection = {}
        for product in r.json():
            self.collection[product['id']] = product
    
    def get(self, productId: int):
        return self.collection.get(productId)
    
    def get_all(self):
        return [product for _, product in self.collection.items()]