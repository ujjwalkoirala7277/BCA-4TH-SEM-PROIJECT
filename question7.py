# Parse a JSON file representing product details (name, price, quantity) and display the
# details in tabular format
import json

with open("products.json", "r") as file:
    products = json.load(file)

print(f"{'Name':<15} {'Price':<10} {'Quantity':<10}")

for product in products:
    print(
        f"{product['name']:<15} "
        f"{product['price']:<10} "
        f"{product['quantity']:<10}"
    )