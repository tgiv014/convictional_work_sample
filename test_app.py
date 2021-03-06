import pytest
import app

required_product_structure = {
    "code": "string",
    "title": "string",
    "vendor": "string",
    "bodyHtml": "string",
    "variants": [
        {
            "id": "string",
            "title": "string",
            "sku": "string",
            "available": True,
            "inventory_quantity": 0,
            "weight": {
              "value": 0,
              "unit": "string"
            }
        }
    ],
    "images": [
        {
            "source": "string",
            "variantId": "string"
        }
    ]
}

required_inventory_structure = [
    {
        "productId": "string",
        "variantId": "string",
        "stock": 0
    }
]


@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client

# This function recursively checks that the JSON object returned matches our required
# template from contract.yaml
def validate_schema(obj, required_structure, description=''):
    # Confirm that the type is correct
    assert type(obj) == type(required_structure), description

    # Recurse correctly based on our type
    if type(obj) is dict:
        # But first! Assert that only specified keys are present
        for key in obj.keys():
            assert key in required_structure, description

        for key, val in required_structure.items():
            assert key in obj, description
            validate_schema(obj[key], val)

    elif type(obj) is list:
        for subobj in obj:
            validate_schema(subobj, required_structure[0])


def test_get_all_products(client):
    res = client.get('/product')

    assert res.status_code == 200, '/product must always return HTTP 200'
    validate_schema(res.json, [required_product_structure],
                    'Validate "get all products" return structure')


def test_get_one_product(client):
    res = client.get('/product/2000000001')

    assert res.status_code == 200, '/product/<productId> must return 200 if productId exists'
    validate_schema(res.json, required_product_structure,
                    'Validate "get one products" return structure')


def test_get_missing_product(client):
    res = client.get('/product/3000000001')

    assert res.status_code == 404, '/product/<productId> must return 404 if productId does not exist'
    assert res.data == b'product not found'


def test_get_missing_product(client):
    res = client.get('/product/abcde')

    assert res.status_code == 400, '/product/<productId> must return 400 for malformed productIds'
    assert res.data == b'Invalid ID supplied'


def test_inventory(client):
    res = client.get('/store/inventory')

    assert res.status_code == 200, '/store/inventory must always return HTTP 200'
    validate_schema(res.json, required_inventory_structure,
                    'Validate "store inventory" return structure')
