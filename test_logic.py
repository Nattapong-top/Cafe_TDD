from _pytest.raises import raises
from domain.logic import Cafe, DrinkNotInMenu


def test_should_return_tea_and_the_change_of_30_bath_when_buying_tea_with_50_baht():
    cafe = Cafe()
    drink, money = cafe.buy('Tea', 50.0)
    assert (drink, money) == ('Tea', 30.0)

def test_should_return_coffee_and_the_change_of_70_bath_when_buying_coffee_with_100_bath():
    cafe = Cafe()
    drink, money = cafe.buy('Coffee', 100.0)
    assert (drink, money) == ('Coffee', 70.0)

def test_should_raise_DrinkNotInMenu_when_buying_cocoa():
    cafe = Cafe()
    with raises(DrinkNotInMenu):
        cafe.buy('Cocoa',50.0)