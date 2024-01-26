from inventory_report.inventory import Inventory


class Report:
    def add_inventory(self, inventory: Inventory) -> None:
        raise NotImplementedError

    def generate(self) -> str:
        raise NotImplementedError