'''Inventory Management 
Problem Statement: 
Create a dictionary to maintain the stock of products in a shop. 
Example: 
{ 
'Laptop': 15, 
'Mouse': 40, 
'Keyboard': 25, 
'Monitor': 10 
} 
Implement the following: 
• Add a new product.  
• Update the stock of an existing product.  
• Remove a product from inventory.  
• Display products having stock less than 20.  
• Display the total number of items available in the inventory. '''
#------------------------------------------------------------------------------------------------
# Products and their stock
inventory = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

# Display inventory
print("Inventory:", inventory)

# Add a new product
product = input("Enter new product name: ")
stock = int(input("Enter stock: "))
inventory[product] = stock
print("After Adding Product:", inventory)

# Update stock of an existing product
product = input("Enter product name to update: ")

if product in inventory:
    stock = int(input("Enter new stock: "))
    inventory[product] = stock
    print("Stock Updated:", inventory)
else:
    print("Product Not Found")

# Remove a product
product = input("Enter product name to remove: ")

if product in inventory:
    del inventory[product]
    print("Product Removed:", inventory)
else:
    print("Product Not Found")

# Display products having stock less than 20
print("Products with stock less than 20:")
for product in inventory:
    if inventory[product] < 20:
        print(product, ":", inventory[product])

# Display total number of items
total = 0
for product in inventory:
    total = total + inventory[product]
print("Total Items Available:", total)

'''
Output:
Inventory: {'Laptop': 15, 'Mouse': 40, 'Keyboard': 25, 'Monitor': 10}
Enter new product name: Phone
Enter stock: 30
After Adding Product: {'Laptop': 15, 'Mouse': 40, 'Keyboard': 25, 'Monitor': 10, 'Phone': 30}
Enter product name to update: Laptop
Enter new stock: 35
Stock Updated: {'Laptop': 35, 'Mouse': 40, 'Keyboard': 25, 'Monitor': 10, 'Phone': 30}
Enter product name to remove: Keyboard
Product Removed: {'Laptop': 35, 'Mouse': 40, 'Monitor': 10, 'Phone': 30}
Products with stock less than 20:
Monitor : 10
Total Items Available: 115
'''