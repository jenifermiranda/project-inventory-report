from inventory_report.inventory import Inventory


class Report:
    def add_inventory(self, inventory: Inventory) -> None:
        self.inventory = inventory

    def generate(self) -> str:
        raise NotImplementedError