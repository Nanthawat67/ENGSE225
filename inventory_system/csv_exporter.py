import csv
from pathlib import Path
from typing import Iterable
from .models import Product

class CsvReportExporter:
    def export_low_stock(self, products: Iterable[Product], output_path: str) -> Path:
        low_stock = [p for p in products if p.quantity <= p.reorder_point]
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['product_id','name','barcode','quantity','reorder_point'])
            for p in low_stock:
                writer.writerow([p.product_id, p.name, p.barcode or '', p.quantity, p.reorder_point])
        return path
