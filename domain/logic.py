class Cafe:

    PRICE = {
        'Tea': 20.0,
        'Coffee': 30.0}

    def buy(self, drink: str, money: float) -> tuple[str, float]:
        self._validate_drink(drink)
        change = money - self.PRICE[drink]
        return drink, change

    def _validate_drink(self, drink: str):
        if drink not in self.PRICE:
            raise DrinkNotInMenu()


class DrinkNotInMenu(Exception):
    pass