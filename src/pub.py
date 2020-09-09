from src.customer import Customer

class Pub:

    def __init__(self, input_name, input_till):
        self.name = input_name
        self.till = input_till
        self.drinks = []

    def add_drink_to_menu(self, drink):
        self.drinks.append(drink)

    def menu_length(self):
        return len(self.drinks)

    def add_money_to_till(self, amount):
        self.till += amount

    def get_drink_price(self, name):
        for drink in self.drinks:
            if drink.name == name:
                return drink.price

    def sell_drink_to_customer(self, customer, drink):
        if customer.age >= 18:
            price = self.get_drink_price(drink)
            customer.reduce_wallet(price)
            self.add_money_to_till(price)