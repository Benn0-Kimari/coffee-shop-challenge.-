import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer  # or coffee, order, etc.

import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):
    def test_order_initialization(self):
        customer = Customer("John Doe")
        coffee = Coffee("Espresso")
        order = Order(customer, coffee, 3.5)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 3.5)

    def test_price_validation(self):
        customer = Customer("John Doe")
        coffee = Coffee("Espresso")
        with self.assertRaises(ValueError):
            Order(customer, coffee, 0.5)

if __name__ == '__main__':
    unittest.main()