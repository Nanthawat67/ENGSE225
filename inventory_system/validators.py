from typing import Optional

def validate_product_name(name: str) -> str:
    name = name.strip()
    if not name:
        raise ValueError('ชื่อสินค้าห้ามว่าง')
    if len(name) > 100:
        raise ValueError('ชื่อสินค้ายาวเกิน 100 ตัวอักษร')
    return name

def validate_non_negative_int(value: int, field_name: str) -> int:
    if isinstance(value, bool):
        raise ValueError(f'{field_name} ต้องเป็นจำนวนเต็ม')
    try:
        value = int(value)
    except (TypeError, ValueError):
        raise ValueError(f'{field_name} ต้องเป็นจำนวนเต็ม')
    if value < 0:
        raise ValueError(f'{field_name} ต้องไม่ติดลบ')
    return value

def validate_barcode(barcode: Optional[str]) -> Optional[str]:
    if barcode is None:
        return None
    barcode = str(barcode).strip()
    if not barcode:
        return None
    if len(barcode) > 50:
        raise ValueError('Barcode ยาวเกิน 50 ตัวอักษร')
    return barcode
