from pathlib import Path
from .csv_exporter import CsvReportExporter
from .logger import get_logger
from .repository import InventoryRepository
from .service import InventoryService

logger = get_logger()

def print_products(products):
    if not products:
        print('\nไม่พบข้อมูลสินค้า')
        return
    print('\n' + '-' * 88)
    print(f"{'ID':<5}{'ชื่อสินค้า':<24}{'Barcode':<18}{'Stock':>10}{'Reorder':>12}")
    print('-' * 88)
    for p in products:
        print(f"{p.product_id:<5}{p.name[:22]:<24}{(p.barcode or '-'):18}{p.quantity:>10}{p.reorder_point:>12}")
    print('-' * 88)

def read_int(prompt, allow_blank=False):
    raw = input(prompt).strip()
    if allow_blank and raw == '':
        return None
    try:
        return int(raw)
    except ValueError:
        raise ValueError('กรุณากรอกเป็นจำนวนเต็ม')

def main():
    base = Path(__file__).resolve().parent.parent
    service = InventoryService(InventoryRepository(str(base / 'data.json')))
    exporter = CsvReportExporter()
    print('=' * 88)
    print('ENGSE225 - Inventory System')
    print('Software Evolution & Maintenance | Version 2.0.0')
    print('=' * 88)
    while True:
        print('''\n[1] แสดงสินค้าทั้งหมด
[2] ค้นหาสินค้า
[3] เพิ่มสินค้า
[4] แก้ไขสินค้า
[5] รับสินค้าเข้า (Stock In)
[6] ตัดสินค้าออก (Stock Out)
[7] แสดงสินค้า Low Stock
[8] Export Low Stock เป็น CSV
[0] ออกจากโปรแกรม''')
        choice = input('เลือกเมนู: ').strip()
        try:
            if choice == '1': print_products(service.list_products())
            elif choice == '2': print_products(service.search(input('ค้นหาชื่อ / ID / Barcode: ')))
            elif choice == '3':
                p = service.add_product(input('ชื่อสินค้า: '), read_int('จำนวนเริ่มต้น: '), read_int('จุดสั่งซื้อ: '), input('Barcode (เว้นว่างได้): '))
                logger.info('add_product id=%s', p.product_id); print(f'เพิ่มสินค้า #{p.product_id} สำเร็จ')
            elif choice == '4':
                pid = read_int('รหัสสินค้า: '); name = input('ชื่อใหม่ (เว้นว่าง = ไม่เปลี่ยน): ').strip(); reorder = read_int('จุดสั่งซื้อใหม่ (เว้นว่าง = ไม่เปลี่ยน): ', True); barcode = input('Barcode ใหม่ (เว้นว่าง = ไม่เปลี่ยน): ').strip()
                service.update_product(pid, name or None, reorder, barcode or None); logger.info('update_product id=%s', pid); print('แก้ไขสินค้าสำเร็จ')
            elif choice == '5':
                pid = read_int('รหัสสินค้า: '); amount = read_int('จำนวนที่รับเข้า: '); p = service.stock_in(pid, amount); logger.info('stock_in id=%s amount=%s', pid, amount); print(f'Stock ใหม่ของ {p.name}: {p.quantity}')
            elif choice == '6':
                pid = read_int('รหัสสินค้า: '); amount = read_int('จำนวนที่ตัดออก: '); p = service.stock_out(pid, amount); logger.info('stock_out id=%s amount=%s', pid, amount); print(f'Stock ใหม่ของ {p.name}: {p.quantity}')
            elif choice == '7':
                low = service.low_stock(); print_products(low); print(f'จำนวนสินค้า Low Stock: {len(low)} รายการ')
            elif choice == '8':
                out = base / 'exports' / 'low_stock_report.csv'; print(f'Export สำเร็จ: {exporter.export_low_stock(service.list_products(), str(out))}')
            elif choice == '0': print('ปิดโปรแกรม'); break
            else: print('เมนูไม่ถูกต้อง')
        except (ValueError, RuntimeError) as exc:
            logger.warning('operation_failed: %s', exc); print(f'เกิดข้อผิดพลาด: {exc}')

if __name__ == '__main__': main()
