from  product import Product
import pytest

def test_obj_init():
    _=Product(1,'Apple','Fruit',4,5)

def test_prod_name_updation():
    p=Product(1,'Apple','Fruit',4,5)
    p.update_product_name('Mango')
    assert p.name=='Mango'

def test_category_name_updation():
    p=Product(1,'Apple','Veggie',4,5)
    p.update_category_name('Fruit')
    assert p.category=='Fruit'

def test_price_updation():
    p=Product(1,'Apple','Veggie',4,5)
    p.update_price(10)
    assert p.price==10

def test_qty_updation():
    p=Product(1,'Apple','Veggie',4,5)
    p.update_qty(0)
    assert p.qty==0

def test_adjust_qty():
    p=Product(1,'Apple','Veggie',4,5)
    p.adjust_qty(6)
    assert p.qty==10

def test_adjust_qty_error():    
    with pytest.raises(ValueError,match='Qty is becoming negative post adjustment'):
        p=Product(1,'Apple','Veggie',4,5)
        p.adjust_qty(-6)
