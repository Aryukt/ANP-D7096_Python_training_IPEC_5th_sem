'''
 Shopping Cart Billing System
Problem Statement
A supermarket allows a customer to purchase multiple products.
The customer first enters the number of products.
For each product, enter:
• Product Name
• Quantity
• Price per Unit
Finally display:
• Individual Product Cost
• Total Bill Amount
• Most Expensive Product
• Cheapest Product
• Average Product Cost'''
n = int(input("Enter the number of products: "))
products = []
for i in range(n):
    name = input(f"Enter the name of product {i + 1}: ")
    quantity = int(input(f"Enter the quantity of product {i + 1}: "))
    price_per_unit = float(input(f"Enter the price per unit of product {i + 1}: "))
    products.append((name, quantity, price_per_unit))
    product_cost = quantity * price_per_unit
    print(f"Cost of {name}: ₹{product_cost}")

total_bill = sum(quantity * price_per_unit for _, quantity, price_per_unit in products)
most_expensive = max(products, key=lambda x: x[2])
cheapest = min(products, key=lambda x: x[2])
average_cost = total_bill / len(products) if products else 0

print(f"Total Bill Amount: ₹{total_bill}")
print(f"Most Expensive Product: {most_expensive[0]} (₹{most_expensive[2]})")
print(f"Cheapest Product: {cheapest[0]} (₹{cheapest[2]})")
print(f"Average Product Cost: ₹{average_cost}")