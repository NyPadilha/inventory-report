from typing import List, Optional

from inventory_report.product import Product


class Inventory:
    def __init__(self, data: Optional[List[Product]] = None):
        self._data = [] if data == None else data

    def add_data(self, data: List[Product]):
        self._data.extend(data)

    @property
    def data(self) -> List[Product]:
        return self._data.copy()
