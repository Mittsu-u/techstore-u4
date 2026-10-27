import pytest
from decimal import Decimal
from app.domain import Money, OrderStatus, InvalidOrderData, InvalidOrderTransition
from cargar_csv import load_fixture

def test_money_negativo():
    with pytest.raises(InvalidOrderData):
        Money(Decimal("-1"))

def test_pedido_o001_inicia_draft():
    orders = load_fixture()
    order = orders["O001"]
    assert order.status == OrderStatus.DRAFT
    assert order.units == 4
    assert order.total.amount == Decimal("2100.00")

def test_doble_confirmacion_falla():
    orders = load_fixture()
    order = orders["O013"]

    order.confirm() 
    assert order.status == OrderStatus.CONFIRMED
    
    with pytest.raises(InvalidOrderTransition):
        order.confirm()