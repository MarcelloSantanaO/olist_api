import sys
sys.path.append('.')
from src.models.product_model import Product
from src.models.base_model import BaseModel
import pytest


class TestProductModel:
    @pytest.mark.parametrize('name, price, description',
                             [('nome', 50.5, None), ('produto', 6.5, None)])
    def test_product_instance_attributes(self, name, price, description):
        product = Product(name, price, description)

        assert isinstance(product, Product)
        assert isinstance(product, BaseModel)
        assert hasattr(product, 'name')
        assert hasattr(product, 'price')
        assert hasattr(product, 'description')
        assert product.name == name
        assert product.price == price
        assert product.description == description

    def test_product_name_empty(self):
        with pytest.raises(ValueError):
            Product('', 5.5, 'descrição')

    def test_product_name_len(self):
        with pytest.raises(ValueError):
            Product('blablabla' * 100, 5.5, 'descrição')

    def test_product_name_int(self):
        with pytest.raises(TypeError):
            Product(100, 5.5, 'descrição')

    def test_price_zero(self):
        with pytest.raises(ValueError):
            Product('blablabla', 0.0, 'descrição')

    def test_price_not_float(self):
        with pytest.raises(TypeError):
            Product('blablabla', '', 'descrição')

    def test_description_len(self):
        with pytest.raises(ValueError):
            Product('blablabla', 5.5, 'descrição' * 255)

    def test_description_int(self):
        with pytest.raises(TypeError):
            Product('blablabla', 5.5, 10)
