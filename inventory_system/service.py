from typing import List, Optional
from .models import Product
from .repository import InventoryRepository
from .validators import validate_barcode, validate_non_negative_int, validate_product_name

class InventoryService:
    def __init__(self, repository: InventoryRepository):
        self.repository = repository
        self.products: List[Product] = self.repository.load()

    def _next_id(self) -> int:
        return max((p.product_id for p in self.products), default=0) + 1

    def _find(self, product_id: int) -> Product:
        for product in self.products:
            if product.product_id == product_id:
                return product
        raise ValueError('ไม่พบสินค้า')

    def save(self) -> None:
        self.repository.save(self.products)

    def list_products(self) -> List[Product]:
        return sorted(self.products, key=lambda p: p.product_id)

    def search(self, keyword: str) -> List[Product]:
        keyword = keyword.strip().lower()
        if not keyword:
            return self.list_products()
        return [p for p in self.list_products() if keyword in p.name.lower() or keyword in str(p.product_id) or keyword in (p.barcode or '').lower()]

    def add_product(self, name: str, quantity: int, reorder_point: int = 0, barcode: Optional[str] = None) -> Product:
        product = Product(
            product_id=self._next_id(),
            name=validate_product_name(name),
            quantity=validate_non_negative_int(quantity, 'จำนวนสินค้า'),
            reorder_point=validate_non_negative_int(reorder_point, 'จุดสั่งซื้อ'),
            barcode=validate_barcode(barcode),
        )
        self.products.append(product)
        self.save()
        return product

    def update_product(self, product_id: int, name: Optional[str] = None, reorder_point: Optional[int] = None, barcode: Optional[str] = None) -> Product:
        product = self._find(product_id)
        if name is not None:
            product.name = validate_product_name(name)
        if reorder_point is not None:
            product.reorder_point = validate_non_negative_int(reorder_point, 'จุดสั่งซื้อ')
        if barcode is not None:
            product.barcode = validate_barcode(barcode)
        self.save()
        return product

    def stock_in(self, product_id: int, amount: int) -> Product:
        amount = validate_non_negative_int(amount, 'จำนวนเพิ่ม')
        if amount == 0:
            raise ValueError('จำนวนเพิ่มต้องมากกว่า 0')
        product = self._find(product_id)
        product.quantity += amount
        self.save()
        return product

    def stock_out(self, product_id: int, amount: int) -> Product:
        amount = validate_non_negative_int(amount, 'จำนวนตัดออก')
        if amount == 0:
            raise ValueError('จำนวนตัดออกต้องมากกว่า 0')
        product = self._find(product_id)
        if amount > product.quantity:
            raise ValueError('จำนวนตัดออกมากกว่าสินค้าในคลัง')
        product.quantity -= amount
        self.save()
        return product

    def low_stock(self) -> List[Product]:
        return [p for p in self.list_products() if p.quantity <= p.reorder_point]
