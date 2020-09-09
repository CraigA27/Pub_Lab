import unittest
from src.pub import Pub
from src.customer import Customer
from src.drinks import Drinks

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Frodo Baggins", 50, 30.00)
    
    def test_customer_has_name(self):
        self.assertEqual("Frodo Baggins", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(30.00, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(10.00)
        self.assertEqual(20.00, self.customer.wallet)