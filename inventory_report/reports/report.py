from inventory_report.inventory import Inventory
from typing import Protocol

class Report(Protocol):
    def add_inventory(self, inventory: Inventory) -> None:
        raise NotImplementedError

    def generate(self) -> str:
        raise NotImplementedError