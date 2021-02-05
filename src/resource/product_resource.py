from flask_restful import fields, marshal_with

from src.dao.product_dao import ProductDao
from src.models.product_model import Product
from src.resource.base_resource import BaseResource


class ProductResource(BaseResource):
    fields = {
        "id_": fields.Integer,
        "name": fields.String,
        "description": fields.String,
        "price": fields.Float
    }

    def __init__(self):
        self.__dao = ProductDao()
        self.__model_type = Product

        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id: int = None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id: int):
        return super().put(id)

    @marshal_with(fields)
    def delete(self,id: int):
        return super().delete(id)
