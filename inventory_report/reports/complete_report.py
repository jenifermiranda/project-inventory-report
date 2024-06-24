from inventory_report.reports.simple_report import SimpleReport

class CompleteReport(SimpleReport):
    def generate(self) -> str:
        result = super().generate()
        result += "\nStocked products by company:\n"

        company_name = {}
        for inventory in self.inventories:
            for product in inventory.data:
                if product.company_name in company_name:
                    company_name[product.company_name] += 1
                else:
                    company_name[product.company_name] = 1
        
        for company, count in company_name.items():
            result += f"- {company}: {count}\n"

        return result
