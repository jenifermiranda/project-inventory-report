from inventory_report.product import Product

def test_create_product() -> None:
    product = Product(
        id="123",
        product_name="Product-name",
        company_name="Company-name",
        manufacturing_date="2024-01-01",
        expiration_date="2024-01-25",
        serial_number="123456",
        storage_instructions="Keep in a dry and cool place",
    )

    assert product.id == "123"
    assert product.product_name == "Product-name"
    assert product.company_name == "Company-name"
    assert product.manufacturing_date == "2024-01-01"
    assert product.expiration_date == "2024-01-25"
    assert product.serial_number == "123456"
    assert product.storage_instructions == "Keep in a dry and cool place"

