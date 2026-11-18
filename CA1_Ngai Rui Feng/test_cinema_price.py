import pytest

from cinema_price import ticket_price


# CT-TP-001: price of one or more tickets = ticket_count x 1200 cents
@pytest.mark.parametrize(
    "ticket_count, expected",
    [
        (1, 1200),
        (2, 2400),
        (5, 6000),
    ],
)
def test_ct_tp_001_price_is_count_times_1200(ticket_count, expected):
    assert ticket_price(ticket_count) == expected


# CT-TP-002: zero tickets costs zero (lower boundary)
def test_ct_tp_002_zero_tickets_costs_zero():
    assert ticket_price(0) == 0


# CT-TP-003: result is an int in whole cents
def test_ct_tp_003_result_is_int():
    result = ticket_price(3)
    assert result == 3600
    assert type(result) is int


# CT-TP-004: negative ticket count -> ValueError
@pytest.mark.parametrize("ticket_count", [-1])
def test_ct_tp_004_negative_count_raises_value_error(ticket_count):
    with pytest.raises(ValueError):
        ticket_price(ticket_count)


# CT-TP-005: non-int ticket count -> TypeError
@pytest.mark.parametrize("ticket_count", [2.5, 3.0, "3", None, [1]])
def test_ct_tp_005_non_int_raises_type_error(ticket_count):
    with pytest.raises(TypeError):
        ticket_price(ticket_count)


# CT-TP-006: boolean ticket count -> TypeError
@pytest.mark.parametrize("ticket_count", [True, False])
def test_ct_tp_006_bool_raises_type_error(ticket_count):
    with pytest.raises(TypeError):
        ticket_price(ticket_count)
