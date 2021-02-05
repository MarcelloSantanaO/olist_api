from flask import Flask
from flask_restful import Api
from src.resource.product_resource import ProductResource

app = Flask(__name__)

api = Api(app)

api.add_resource(ProductResource, '/api/product', endpoint='Products')
api.add_resource(ProductResource, '/api/product/<int:id>', endpoint='Product')

app.run(debug=True)
