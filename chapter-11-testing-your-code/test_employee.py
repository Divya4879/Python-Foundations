import pytest

from employee import Employee

def test_give_default_raise():
    divya = Employee('Divya', 'Singh',25_000)
    divya.give_raise()
    assert divya.salary == 30_000

def test_give_custom_raise():
    ria = Employee('Ria', 'Singh',15_000)
    ria.give_raise(10_000)
    assert ria.salary == 25_000


# Above tests using fixture

@pytest.fixture
def give_x_raise():
    khushi = Employee('Khushi', 'Singhania', 50_000)
    return khushi

def test_give_default_raise(give_x_raise):
    give_x_raise.give_raise()
    assert give_x_raise.salary == 55_000

def test_give_custom_raise(give_x_raise):
    give_x_raise.give_raise(10_000)
    """
    Why didn't the salary increase from the test_give_default_raise()?
    Coz it's just a test().
    Doesn't get called, doesn't run, just there for testing:))
    """
    assert give_x_raise.salary == 60_000 