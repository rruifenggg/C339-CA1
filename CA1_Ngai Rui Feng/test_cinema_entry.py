import pytest

from cinema_entry import can_watch


# CT-CW-001: customers below age 16 may not watch
@pytest.mark.parametrize("age", [15])
def test_ct_cw_001_below_16_not_allowed(age):
    assert can_watch(age) is False


# CT-CW-002: exactly age 16 may watch
def test_ct_cw_002_exactly_16_allowed():
    assert can_watch(16) is True


# CT-CW-003: above age 16 may watch
@pytest.mark.parametrize("age", [17])
def test_ct_cw_003_above_16_allowed(age):
    assert can_watch(age) is True


# CT-CW-004: result is a Python bool
@pytest.mark.parametrize("age, expected", [(15, False), (16, True)])
def test_ct_cw_004_result_is_bool(age, expected):
    result = can_watch(age)
    assert result == expected
    assert type(result) is bool


# CT-CW-005: negative age -> ValueError
@pytest.mark.parametrize("age", [-1])
def test_ct_cw_005_negative_age_raises_value_error(age):
    with pytest.raises(ValueError):
        can_watch(age)


# CT-CW-006: non-int age -> TypeError
@pytest.mark.parametrize("age", [16.5, 16.0, "16", None])
def test_ct_cw_006_non_int_raises_type_error(age):
    with pytest.raises(TypeError):
        can_watch(age)


# CT-CW-007: boolean age -> TypeError
@pytest.mark.parametrize("age", [True, False])
def test_ct_cw_007_bool_raises_type_error(age):
    with pytest.raises(TypeError):
        can_watch(age)
