import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer  # or coffee, order, etc.


import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_customer_initialization(self):
        customer = Customer("John Doe")
        self.assertEqual(customer.name, "John Doe")

    def test_customer_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("A" * 16)

    def test_create_order(self):
        customer = Customer("John Doe")
        coffee = Coffee("Espresso")
        order = customer.create_order(coffee, 3.5)
        self.assertIsInstance(order, Order)
        self.assertIn(order, customer.orders())

    def test_coffees(self):
        customer = Customer("John Doe")
        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")
        customer.create_order(coffee1, 3.5)
        customer.create_order(coffee2, 4.0)
        self.assertIn(coffee1, customer.coffees())
        self.assertIn(coffee2, customer.coffees())

if __name__ == '__main__':
    unittest.main()