from src.analyze import (
    calc_high_spending_count,
    calc_monthly_cumulative_sales,
)
from src.client import Client
from src.sale import Sale


def _sales():
    return [
        Sale("S1", 1, "Laptop", "Electronics", 600.0, "2023-07-01"),
        Sale("S2", 1, "Mouse", "Accessories", 20.0, "2023-08-02"),
    ]


def test_high_spending_count():
    clients = [
        Client(1, "Ana", "Spain", "2022-01-01"),
        Client(2, "Luis", "Spain", "2022-01-01"),
    ]
    assert calc_high_spending_count(clients, _sales()) == 1


def test_monthly_cumulative_sales():
    assert calc_monthly_cumulative_sales(_sales()) == {"2023-07": 600.0, "2023-08": 620.0}


def test_client_to_dict():
    assert Client(1, "Ana", "Spain", "2022-01-01").to_dict()["name"] == "Ana"