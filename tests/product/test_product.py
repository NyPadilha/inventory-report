from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        id="2427",
        product_name="voluptas",
        company_name="da Cruz Costela e Filhos",
        manufacturing_date="2023-12-28",
        expiration_date="2066-08-30",
        serial_number="YU63 PJ8Q 2659 2SJ9 77H8 491M 0W43",
        storage_instructions="Eos expedita odit voluptates amet eaque. Sequi sunt nam voluptatibus doloremque odit. Ea voluptate reiciendis officia omnis.",
    )

    assert product.id == "2427"
    assert product.product_name == "voluptas"
    assert product.company_name == "da Cruz Costela e Filhos"
    assert product.manufacturing_date == "2023-12-28"
    assert product.expiration_date == "2066-08-30"
    assert product.serial_number == "YU63 PJ8Q 2659 2SJ9 77H8 491M 0W43"
    assert (
        product.storage_instructions
        == "Eos expedita odit voluptates amet eaque. Sequi sunt nam voluptatibus doloremque odit. Ea voluptate reiciendis officia omnis."
    )
