from models import Product, ProductDetails
import base64
from django.core.files.base import ContentFile

class DBHandler(object):

    @classmethod
    def process_products(self, product_data, user, pk=None):
        defaults = {
            'name': product_data.get('name')
        }
        product, created = Product.objects.update_or_create(defaults=defaults, name=product_data.get('name'))
        return product

    @classmethod
    def process_product_details(self, product_details, user, pk=None):
        defaults = {}
        data = None
        product_id = product_details.get('product')
        defaults['product'] = Product.objects.get(pk=product_id)

        defaults['category'] = product_details.get('category')
        defaults['price'] = product_details.get('price')
        image_data = product_details.get('image')
        file_name=image_data.split('/')[-1] or None
        with open(image_data, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            decoded_file = base64.b64decode(encoded_string)
            data = ContentFile(decoded_file, name=file_name)
        print data
        defaults['image'] = data
        defaults['description'] = product_details.get('description')
        defaults['rating'] = product_details.get('rating')
        defaults['availability'] = product_details.get('availability') or False
        product_details, created = ProductDetails.objects.update_or_create(defaults=defaults, product=product_details.get('product'), category=product_details.get('category'))
        return product_details
