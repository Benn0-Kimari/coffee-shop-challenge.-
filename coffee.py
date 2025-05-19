class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
        self._name = name
        self._orders = []  # <-- This fixes the error!

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Coffee name is immutable and cannot be changed.")

    def orders(self):
        return self._orders

    def customers(self):
        return list({order.customer for order in self._orders})
