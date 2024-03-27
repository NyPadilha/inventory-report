# Inventory Report (Trybe Project)

Report generator. The goal is to receive files containing information about a specific stock and then produce a comprehensive report based on that data. This stock data can be obtained from two sources:

By importing a CSV file;

By importing a JSON file;

🚵 Worked Skills:

- Apply Object Oriented Programming concepts in Python.
- Implement reading and writing CSV and JSON files in Python.

<details>
    <summary><strong>Portuguese Description</strong></summary></br>

    Gerador de relatórios. O objetivo é receber arquivos contendo informações sobre um estoque específico e, em seguida, produzir um relatório abrangente com base nesses dados. Esses dados de estoque poderão ser obtidos de duas fontes:

    Através da importação de um arquivo CSV;

    Através da importação de um arquivo JSON;

    🚵 Habilidades a serem trabalhadas:

    - Aplicar conceitos de Programação Orientada a Objetos em Python.
    - Implementar leitura e escrita de arquivos CSV e JSON em Python.

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