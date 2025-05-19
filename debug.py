from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
order1 = Order(alice, latte, 4.5)
order2 = Order(alice, espresso, 3.0)
order3 = Order(bob, latte, 5.0)

# Inspect orders
print(f"{alice.name}'s orders:")
for order in alice.orders():
    print(f" - {order.coffee.name} at ${order.price}")

print(f"\nCoffees ordered by {alice.name}:")
for coffee in alice.coffees():
    print(f" - {coffee.name}")

print(f"\nCustomers who ordered {latte.name}:")
for customer in latte.customers():
    print(f" - {customer.name}")

print(f"\n{latte.name} has {latte.num_orders()} order(s).")
print(f"Average price of {latte.name}: ${latte.average_price():.2f}")

# Bonus method (if implemented)
most_spent = Customer.most_aficionado(latte)
if most_spent:
    print(f"\nMost aficionado of {latte.name}: {most_spent.name}")
else:
    print(f"\nNo one has ordered {latte.name} yet.")
