import json
from abc import ABC, abstractmethod
from typing import Dict, List, Type

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            data = json.load(file)
            products = []
            for product in data:
                products.append(
                    Product(
                        product["id"],
                        product["product_name"],
                        product["company_name"],
                        product["manufacturing_date"],
                        product["expiration_date"],
                        product["serial_number"],
                        product["storage_instructions"],
                    )
                )
            return products


# Não altere a variável abaixo
IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
}
