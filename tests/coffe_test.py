import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from customer import Customer  # or coffee, order, etc.

import unittest
from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def test_coffee_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("ab")  # Too short
