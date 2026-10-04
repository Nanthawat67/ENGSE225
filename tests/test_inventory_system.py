import json
import pytest
from inventory_system.csv_exporter import CsvReportExporter
from inventory_system.models import Product
from inventory_system.repository import InventoryRepository
from inventory_system.service import InventoryService

def make_service(tmp_path):
    return InventoryService(InventoryRepository(str(tmp_path / 'data.json')))

def test_add_product(tmp_path):
    s = make_service(tmp_path); p = s.add_product('Keyboard', 10, 3, '88500001')
    assert (p.product_id,p.quantity,p.reorder_point,p.barcode) == (1,10,3,'88500001')

def test_stock_in(tmp_path):
    s=make_service(tmp_path); p=s.add_product('Mouse',5,2); s.stock_in(p.product_id,7); assert s.list_products()[0].quantity==12

def test_stock_out(tmp_path):
    s=make_service(tmp_path); p=s.add_product('Mouse',5,2); s.stock_out(p.product_id,3); assert s.list_products()[0].quantity==2

def test_stock_out_cannot_exceed_stock(tmp_path):
    s=make_service(tmp_path); p=s.add_product('Mouse',5,2)
    with pytest.raises(ValueError): s.stock_out(p.product_id,6)

def test_low_stock_uses_reorder_point(tmp_path):
    s=make_service(tmp_path); s.add_product('A',2,5); s.add_product('B',8,5); assert [p.name for p in s.low_stock()]==['A']

def test_search_by_name_and_barcode(tmp_path):
    s=make_service(tmp_path); s.add_product('Keyboard',5,2,'KB001'); assert len(s.search('key'))==1; assert len(s.search('KB001'))==1

def test_old_schema_without_new_fields_is_compatible(tmp_path):
    path=tmp_path/'data.json'; path.write_text(json.dumps([{'id':1,'name':'Old Product','q':7}]),encoding='utf-8'); p=InventoryRepository(str(path)).load()[0]
    assert (p.product_id,p.name,p.quantity,p.barcode,p.reorder_point)==(1,'Old Product',7,None,0)

def test_atomic_save_writes_valid_json(tmp_path):
    path=tmp_path/'data.json'; InventoryRepository(str(path)).save([Product(1,'Test',4,2,'B001')]); payload=json.loads(path.read_text(encoding='utf-8')); assert payload['schema_version']==2; assert payload['products'][0]['name']=='Test'

def test_csv_export_contains_low_stock(tmp_path):
    out=tmp_path/'low.csv'; CsvReportExporter().export_low_stock([Product(1,'A',2,5,'A001'),Product(2,'B',10,5,'B001')],str(out)); content=out.read_text(encoding='utf-8-sig'); assert 'A' in content and '2' in content and 'B' not in content

def test_update_product(tmp_path):
    s=make_service(tmp_path); p=s.add_product('Old',1,1); s.update_product(p.product_id,name='New',reorder_point=5); q=s.list_products()[0]; assert (q.name,q.reorder_point)==('New',5)
