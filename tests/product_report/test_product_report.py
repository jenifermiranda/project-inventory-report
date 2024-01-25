from inventory_report.product import Product

def test_product_report() -> None:
    product = Product(
        id="123",
        product_name="Product-name",
        company_name="Company-name",
        manufacturing_date="2024-01-01",
        expiration_date="2024-01-25",
        serial_number="123456",
        storage_instructions="Keep in a dry and cool place",
    )

    assert (
        str(product)
        == "The product 123 - Product-name with serial number 123456 "
        "manufactured on 2024-01-01 by the company Company-name "
        "valid until 2024-01-25 must be stored according to the "
        "following instructions: Keep in a dry and cool place."
    )
