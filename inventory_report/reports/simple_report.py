from collections import Counter
from datetime import date


class SimpleReport:
    def add_inventory(self, inventory):
        self.inventory = inventory

    def generate(self) -> str:
        current_date = date.today()
        oldest_manufacturing_date = None
        closest_expiration_date = None
        company_name = []

        for product in self.inventory.data:
            fabricacao_mais_antiga =  current_date - date.fromisoformat(product.manufacturing_date)

            if oldest_manufacturing_date is None or fabricacao_mais_antiga > oldest_manufacturing_date:
                oldest_manufacturing_date = fabricacao_mais_antiga
            
            validade_mais_proxima = date.fromisoformat(product.expiration_date) - current_date

            if closest_expiration_date is None or validade_mais_proxima < closest_expiration_date:
                closest_expiration_date = validade_mais_proxima
            
            company_name.append(product.company_name)
            counter = Counter(company_name)
            most_common_company = counter.most_common(1)
        
        result = f"Oldest manufacturing date: {current_date - oldest_manufacturing_date}\n"
        result += f"Closest expiration date: {closest_expiration_date + current_date}\n"
        result += f"Company with the largest inventory: {most_common_company[0][0]}\n"

        return result
            

#fabricacao mais antiga: MAX(manufacturing_date - data de hoje)
#validade mais proxima: MIN(expiration_date - data de hoje)