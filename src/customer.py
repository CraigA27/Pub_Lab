class Customer:
    
    def __init__(self, input_name, input_age, input_wallet):
        self.name = input_name
        self.age = input_age
        self.wallet = input_wallet

    def reduce_wallet(self, amount):
        self.wallet -= amount

    