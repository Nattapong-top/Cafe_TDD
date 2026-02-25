class Cafe:

    PRICE = {
        'Tea': 20.0,
        'Coffee': 30.0
    }

    def buy(self, drink: str, money: float) -> tuple[str, float]:
        change = money - self.PRICE[drink]
        return drink, change

