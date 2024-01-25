import json
import csv
from typing import Dict, List, Type
from abc import ABC, abstractmethod

from inventory_report.product import Product

class Importer(ABC):
    def __init__(self, path: str) -> None:
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
            products.append(Product(**product))
        return products

class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, "r") as file:
            csv_reader = csv.DictReader(file)
            products = []
            for product in csv_reader:
                products.append(Product(**product))
            return products
        


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
