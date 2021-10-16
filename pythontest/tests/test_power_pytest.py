import pytest

from power import power, times, divide


# def test_power():
#     base = 2
#     exp = 3
#     assert power(base, exp) == 8
#     with pytest.raises(TypeError):
#         power("3", "2")
#
#
# def test_times():
#     num1 = 2
#     num2 = 3
#     assert times(num1, num2) == 6


def test_divide():
    num1 = 10
    num2 = 2
    assert divide(num1, num2) == 5


def test_divide_by_zero():
    num1 = 10
    num2 = 0
    # with pytest.raises(ZeroDivisionError):  # この書き方では間違い。Noneが返ってくることを想定して書く。
    #     divide(num1, num2)
    assert divide(num1, num2) is None