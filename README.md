# ENGSE225 - Inventory System

ระบบจัดการคลังสินค้าแบบ Console/CLI สำหรับงาน Software Evolution & Maintenance

## ฟีเจอร์
- Product: product_id, name, quantity, reorder_point, barcode
- Product / InventoryService / InventoryRepository
- Input Validation
- Stock In / Stock Out
- Low Stock ตาม Reorder Point
- Search ตามชื่อ / ID / Barcode
- CR-01: Barcode + Reorder Point
- CR-02: CSV Export สำหรับ Low Stock
- Backward compatibility กับ data.json รุ่นเก่า
- Atomic File Writing ด้วย temporary file + os.replace()
- PyTest เป็น Safety Net
- Logging การทำงานสำคัญ

## รัน
```bash
python -m pip install -r requirements.txt
python -m inventory_system.main
```

## Test
```bash
pytest -q
```

## Demo
1. แสดงสินค้า
2. เพิ่มสินค้า + Barcode + Reorder Point
3. Stock In
4. Stock Out
5. แสดง Low Stock
6. Export CSV
7. ปิด/เปิดใหม่เพื่อดู Persistence
8. รัน pytest
