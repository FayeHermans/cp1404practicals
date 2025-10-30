"""
Week 6: practice
"""

products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]

on_sale_products = [product for product in products if product[2]]
print(on_sale_products)
for thing in products[0]:
    print(thing)