import json, os
from pathlib import Path
from typing import List, Dict, Any
from .models import Product

class InventoryRepository:
    def __init__(self, file_path: str = 'data.json'):
        self.file_path = Path(file_path)

    def load(self) -> List[Product]:
        if not self.file_path.exists():
            return []
        try:
            with self.file_path.open('r', encoding='utf-8') as f:
                raw = json.load(f)
        except json.JSONDecodeError as exc:
            raise RuntimeError('data.json ไม่ใช่ JSON ที่ถูกต้อง') from exc
        if isinstance(raw, dict):
            records = raw.get('products', [])
        elif isinstance(raw, list):
            records = raw
        else:
            raise RuntimeError('โครงสร้าง data.json ไม่ถูกต้อง')
        products = []
        for record in records:
            product = Product.from_dict(record)
            if product.product_id == 0 or not product.name:
                continue
            products.append(product)
        return products

    def save(self, products: List[Product]) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        payload: Dict[str, Any] = {'schema_version': 2, 'products': [p.to_dict() for p in products]}
        temp_path = self.file_path.with_suffix(self.file_path.suffix + '.tmp')
        with temp_path.open('w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp_path, self.file_path)
