import unittest
from src.pub import Pub
from src.customer import Customer
from src.drinks import Drinks


class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        pub_name = self.pub.name
        self.assertEqual("The Prancing Pony", pub_name)

    def test_pub_has_till(self):
        pub_till = self.pub.till
        self.assertEqual(100.00, pub_till)

    def test_pub_has_drinks_list(self):
        drink_1 = Drinks("Stella", 3.50)
        self.pub.add_drink_to_menu(drink_1)
        self.assertEqual(1, self.pub.menu_length())

    def test_add_to_till(self):
        self.pub.add_money_to_till(10.00)
        self.assertEqual(110.00, self.pub.till)  

    def test_get_drink_price(self):
        drink_1 = Drinks("Stella", 3.50)
        self.pub.add_drink_to_menu(drink_1)
        price = self.pub.get_drink_price("Stella")
        self.assertEqual(3.50, price)       

    def   test_sell_drink_to_customer_wallet(self):
            drink_1 = Drinks("Stella", 3.50)
            customer = Customer("Frodo Baggins", 50, 30.00)
            self.pub.add_drink_to_menu(drink_1)
            self.pub.sell_drink_to_customer(customer, "Stella")
            self.assertEqual(26.50, customer.wallet)

    def test_sell_drink_to_customer_till(self):
            drink_1 = Drinks("Stella", 3.50)
            customer = Customer("Frodo Baggins",50, 30.00)
            self.pub.add_drink_to_menu(drink_1)
            self.pub.sell_drink_to_customer(customer, "Stella")
            self.assertEqual(103.50, self.pub.till)   


    