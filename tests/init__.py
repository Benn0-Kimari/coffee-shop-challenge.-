class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []  # necessary for create_order
