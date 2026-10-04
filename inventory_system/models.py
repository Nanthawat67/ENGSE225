from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any

@dataclass
class Product:
    product_id: int
    name: str
    quantity: int
    reorder_point: int = 0
    barcode: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Product':
        return cls(
            product_id=int(data.get('product_id', data.get('id', 0))),
            name=str(data.get('name', '')).strip(),
            quantity=int(data.get('quantity', data.get('q', 0))),
            reorder_point=int(data.get('reorder_point', data.get('r', 0))),
            barcode=data.get('barcode', data.get('b')),
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
