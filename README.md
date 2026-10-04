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

---

## 15. ผลทดสอบ

1

<img width="633" height="340" alt="image" src="https://github.com/user-attachments/assets/b1f7fcb7-bb6d-4424-959c-3c6af69eff7c" />


2

<img width="636" height="300" alt="image" src="https://github.com/user-attachments/assets/095b5f99-2df7-4139-a365-b9828b553ab4" />


3

<img width="634" height="616" alt="image" src="https://github.com/user-attachments/assets/dc121a70-455b-4b05-bf80-9d34fbb26a51" />


4

<img width="633" height="621" alt="image" src="https://github.com/user-attachments/assets/79251c4c-1145-4832-89d4-5af6074b4c69" />


5

<img width="629" height="583" alt="image" src="https://github.com/user-attachments/assets/50e4b5a4-bfe2-4c2f-ab42-707dc26321ee" />


6

<img width="628" height="584" alt="image" src="https://github.com/user-attachments/assets/6ea73aca-44d5-43d7-9cbb-efe42d21cfac" />


7

<img width="633" height="315" alt="image" src="https://github.com/user-attachments/assets/8d1bd46d-3fc2-4416-b9f7-98fe5c7fb96b" />


8

<img width="597" height="200" alt="image" src="https://github.com/user-attachments/assets/30e39826-a20c-4ed6-851b-2da401b0c4c0" />


9

<img width="217" height="195" alt="image" src="https://github.com/user-attachments/assets/f9059cf4-9c23-496b-a5ef-816d61332c29" />
