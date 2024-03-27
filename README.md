# Inventory Report (Trybe Project)

???

🚵 Worked Skills:

- 

<details>
    <summary><strong>Portuguese Description</strong></summary></br>

    Neste projeto, irá desenvolver um gerador de relatórios. O objetivo é receber arquivos contendo informações sobre um estoque específico e, em seguida, produzir um relatório abrangente com base nesses dados. Esses dados de estoque poderão ser obtidos de duas fontes:

    Através da importação de um arquivo CSV;

    Através da importação de um arquivo JSON;

    Além disso, o relatório final possuirá duas versões: simples e completa.

    🚵 Habilidades a serem trabalhadas:

    - 
</details>

<br>

<details>
    <summary><strong>How to run</strong></summary></br>

    1. Clone this repository with:

        - `git clone git@github.com:NyPadilha/inventory-report.git`
        - `cd  inventory-report`

    Using Venv:

        1. Create the Virtual Environment:

            - `python3 -m venv .venv && source .venv/bin/activate`

        2. Install the dependencies:

            - `python3 -m pip install -r dev-requirements.txt`

    Without Venv:

        1. Install dependencies with:

            - `python3 -m pip install -r dev-requirements.txt`

    Test:

        `python3 -m pytest`
</details>

<br>

## What I Coded

- inventory_report/importers.py
- inventory_report/inventory.py
- inventory_report/reports/report.py
- tests/product/test_product.py
- tests/product_report/test_product_report.py

## What Trybe Coded

- Basically everything else