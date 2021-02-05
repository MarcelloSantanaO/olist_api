import sys
sys.path.append('.')
from sqlalchemy.orm.exc import UnmappedInstanceError
from src.dao.product_dao import ProductDao
from src.models.product_model import Product
import pytest


class TestProductDao:
    @pytest.fixture
    def product_instance(self):
        product = Product('Produto', 50.5, 'Descrição')
        return product

    def test_instance(self):
        product_dao = ProductDao()
        assert isinstance(product_dao, ProductDao)

    def test_save(self, product_instance):
        product_saved = ProductDao().save(product_instance)

        assert product_saved.id_ is not None
        ProductDao().delete(product_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            ProductDao().save('Produto')

    def test_read_by_id(self, product_instance):
        product_saved = ProductDao().save(product_instance)
        product_read = ProductDao().read_by_id(product_saved.id_)

        assert isinstance(product_read, Product)
        ProductDao().delete(product_saved)

    def test_read_by_id_invalid(self):
        with pytest.raises(TypeError):
            product_read = ProductDao().read_by_id('id')

    def test_read_all(self):
        product_read = ProductDao().read_all()

        assert isinstance(product_read, list)

    def test_delete(self, product_instance):
        product_saved = ProductDao().save(product_instance)
        product_read = ProductDao().read_by_id(product_saved.id_)
        ProductDao().delete(product_read)
        product_read = ProductDao().read_by_id(product_saved.id_)

        assert product_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            ProductDao().delete('Produtp')
