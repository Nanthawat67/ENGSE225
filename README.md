# ENGSE225 — Inventory System Evolution

ระบบจัดการคลังสินค้าแบบ Command Line Application ที่พัฒนาต่อจากระบบเดิม โดยเน้นการ **Software Evolution and Maintenance** ผ่านการ Refactoring, การเพิ่ม Change Request, การจัดการ Stock, การตรวจสอบข้อมูล และการสร้าง Automated Tests เพื่อเป็น Safety Net สำหรับการแก้ไขระบบ

**Version:** 2.0.0
**Language:** Python
**Testing:** PyTest
**Data Storage:** JSON
**Export:** CSV

---

## 1. Project Overview

โครงการนี้เป็นการปรับปรุงและวิวัฒนาการระบบจัดการคลังสินค้าเดิมให้สามารถดูแลและพัฒนาต่อได้ง่ายขึ้น โดยแบ่งโครงสร้างของระบบออกเป็นส่วนที่มีหน้าที่ชัดเจน ได้แก่

* Model — จัดการข้อมูลสินค้า
* Service — จัดการ Business Logic
* Repository — จัดการการอ่านและบันทึกข้อมูล
* Validator — ตรวจสอบข้อมูลก่อนดำเนินการ
* CSV Exporter — ส่งออกข้อมูล Low Stock
* Logger — บันทึกเหตุการณ์ของระบบ
* Tests — ตรวจสอบการทำงานของระบบ

---

## 2. Software Evolution

### AS-IS

ระบบเดิมมีโครงสร้างที่รวมความรับผิดชอบหลายส่วนไว้ด้วยกัน ทำให้การแก้ไขหรือเพิ่มความสามารถใหม่ทำได้ยาก และมีความเสี่ยงที่จะกระทบการทำงานเดิม

### TO-BE

ระบบได้รับการปรับโครงสร้างใหม่ให้แยกความรับผิดชอบอย่างชัดเจน พร้อมเพิ่ม Automated Tests เพื่อช่วยตรวจสอบว่าการเปลี่ยนแปลงไม่ทำให้ฟังก์ชันเดิมเสียหาย

ผลลัพธ์คือระบบสามารถ:

* เพิ่มและแก้ไขข้อมูลสินค้า
* ค้นหาสินค้า
* รับสินค้าเข้า Stock
* ตัดสินค้าออกจาก Stock
* ตรวจสอบสินค้า Low Stock
* บันทึกข้อมูลลง JSON
* Export รายการ Low Stock เป็น CSV
* ตรวจสอบการทำงานด้วย Automated Tests

---

## 3. Change Requests

### CR-01: Barcode + Reorder Point

เพิ่มข้อมูล **Barcode** และ **Reorder Point** ให้กับสินค้า เพื่อช่วยระบุสินค้าและกำหนดจุดแจ้งเตือนเมื่อสินค้าเหลือน้อย

กฎ Low Stock:

```text
stock <= reorder_point
```

ตัวอย่าง:

```text
Mouse
Stock: 4
Reorder Point: 5

สถานะ: Low Stock
```

---

### CR-02: CSV Export for Low Stock

เพิ่มความสามารถในการส่งออกรายการสินค้าที่อยู่ในสถานะ Low Stock เป็นไฟล์ CSV เพื่อใช้เป็นรายงานหรือประกอบการตรวจสอบ Stock

ไฟล์ Export:

```text
exports/low_stock_report.csv
```

---

## 4. Stock Management

ระบบรองรับการจัดการ Stock หลัก 2 รูปแบบ

### Stock In

เพิ่มจำนวนสินค้าเข้าสู่คลัง

ตัวอย่างที่ตรวจสอบจริง:

```text
Monitor: 10 → 15
```

### Stock Out

ตัดจำนวนสินค้าออกจากคลัง

ตัวอย่างที่ตรวจสอบจริง:

```text
Monitor: 15 → 3
```

ระบบมีการตรวจสอบข้อมูลก่อนเปลี่ยนแปลง Stock เพื่อป้องกันค่าที่ไม่ถูกต้อง

---

## 5. Testing

ระบบใช้ **PyTest** เป็น Automated Testing เพื่อทำหน้าที่เป็น Safety Net สำหรับการพัฒนาและ Refactoring

ผลการทดสอบที่ตรวจสอบแล้ว:

```text
10 passed in 0.10s
```

การทดสอบครอบคลุมการทำงานสำคัญของระบบ เช่น

* Product Management
* Validation
* Stock In
* Stock Out
* Low Stock
* Reorder Point
* Data Persistence
* CSV Export

---

## 6. Data Persistence

ข้อมูลสินค้าถูกจัดเก็บในไฟล์:

```text
data.json
```

มีการตรวจสอบการทำงานโดยปิดและเปิดโปรแกรมใหม่ และตรวจสอบว่าสินค้าที่เพิ่มและการเปลี่ยนแปลง Stock ยังคงอยู่

---

## 7. Project Structure

```text
ENGSE225_Inventory_System/
│
├── inventory_system/
│   ├── __init__.py
│   ├── models.py
│   ├── validators.py
│   ├── repository.py
│   ├── service.py
│   ├── csv_exporter.py
│   ├── logger.py
│   └── main.py
│
├── tests/
│   ├── conftest.py
│   └── test_inventory_system.py
│
├── exports/
│   └── low_stock_report.csv
│
├── data.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 8. Installation

Clone repository:

```bash
git clone https://github.com/Nanthawat67/Inventory-System.git
cd Inventory-System
```

สร้าง Virtual Environment:

```bash
python -m venv .venv
```

เปิดใช้งาน Virtual Environment:

### Linux / WSL

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

ติดตั้ง dependencies:

```bash
pip install -r requirements.txt
```

---

## 9. Run Application

รันระบบด้วย:

```bash
python -m inventory_system.main
```

เมนูหลักของระบบ:

```text
1. แสดงสินค้าทั้งหมด
2. ค้นหาสินค้า
3. เพิ่มสินค้า
4. แก้ไขสินค้า
5. รับสินค้าเข้า (Stock In)
6. ตัดสินค้าออก (Stock Out)
7. แสดงสินค้า Low Stock
8. Export Low Stock เป็น CSV
0. ออกจากโปรแกรม
```

---

## 10. Run Tests

รัน Automated Tests:

```bash
pytest -q
```

ผลการทดสอบที่ตรวจสอบแล้ว:

```text
10 passed in 0.10s
```

---

## 11. Verified Release Evidence

ระบบ Version 2.0.0 ได้ตรวจสอบ Workflow สำคัญแล้ว ได้แก่

| รายการ              | ผลการตรวจสอบ                      |
| ------------------- | --------------------------------- |
| Application Version | 2.0.0                             |
| Automated Tests     | 10 passed                         |
| Stock In            | Monitor 10 → 15                   |
| Stock Out           | Monitor 15 → 3                    |
| Low Stock           | ทำงานตาม `stock <= reorder_point` |
| CSV Export          | ทำงานสำเร็จ                       |
| Data Persistence    | ตรวจสอบหลัง Restart แล้ว          |
| GitHub              | Version 2.0.0 ถูก Push แล้ว       |

---

## 12. Git Branches

Branch หลักสำหรับ Version ปัจจุบัน:

```text
develop
```

Development branch:

```text
evolution-v2
```

Branch สำหรับเก็บ Version เดิม:

```text
old-develop
```

Version 2.0.0 ใช้ Commit:

```text
d4e1933 feat: evolve inventory system to v2.0.0
```

---

## 13. Technologies

* Python
* PyTest
* JSON
* CSV
* Git
* GitHub

---

## 14. Project Goal

เป้าหมายของโครงการคือการนำแนวคิด **Software Evolution and Maintenance** มาใช้กับระบบที่มีอยู่จริง โดยไม่ได้มุ่งเน้นเพียงการเพิ่มฟังก์ชัน แต่รวมถึงการปรับปรุงโครงสร้างซอฟต์แวร์ การลดความซับซ้อน การเพิ่มความสามารถในการทดสอบ และการสร้าง Safety Net เพื่อให้ระบบสามารถแก้ไขและพัฒนาต่อได้อย่างปลอดภัย

**ENGSE225 — Software Evolution and Maintenance**
