# The functions in this file serve as stand-ins for the logic that would normally
# be handled by a ORM/ODM. We are only translating the internal database format to
# The API-spec data format.

# Giving this a slightly different name because it is not a direct object mapping
def build_images_schema(variants):
    images = []
    for variant in variants:
        for image in variant['images']:
            images.append(
                {
                    'source': image['src'],
                    'variantId': str(variant['id'])
                }
            )
    return images

def build_weight_schema(variant):
    return {
        'value': variant['weight'],
        'unit': variant['weight_unit']
    }

def map_variant_schema(variant):
    return {
        'id': str(variant['id']),
        'title': variant['title'],
        'sku': variant['sku'],
        'available': (variant.get('inventory', 0) > 0),
        'inventory_quantity': variant.get('inventory', 0),
        'weight': build_weight_schema(variant)
    }

def map_product_schema(product):
    return {
        'code': str(product['id']), # This mapping is an assumption. There is not a code/UPC field in the sample JSON
        'title': product['title'],
        'vendor': product['vendor'],
        'bodyHtml': product['body_html'],
        'variants': [map_variant_schema(var) for var in product['variants']],
        'images': build_images_schema(product['variants'])
    }

def map_inventory_schema(products):
    inventory = []
    for product in products:
            for variant in product['variants']:
                inventory.append(
                    {
                        'productId': str(product['id']),
                        'variantId': str(variant['id']),
                        'stock': 0 # There does not appear to be a stock-related field in the sample JSON
                    }
                )
    return inventory