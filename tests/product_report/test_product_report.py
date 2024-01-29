from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        id="2427",
        product_name="voluptas",
        company_name="da Cruz Costela e Filhos",
        manufacturing_date="2023-12-28",
        expiration_date="2066-08-30",
        serial_number="YU63 PJ8Q 2659 2SJ9 77H8 491M 0W43",
        storage_instructions="Eos expedita odit voluptates amet eaque. Sequi sunt nam voluptatibus doloremque odit. Ea voluptate reiciendis officia omnis.",
    )

    assert (
        str(product)
        == "The product 2427 - voluptas with serial number YU63 PJ8Q 2659 2SJ9 77H8 491M 0W43 manufactured on 2023-12-28 by the company da Cruz Costela e Filhos valid until 2066-08-30 must be stored according to the following instructions: Eos expedita odit voluptates amet eaque. Sequi sunt nam voluptatibus doloremque odit. Ea voluptate reiciendis officia omnis.."
    )
