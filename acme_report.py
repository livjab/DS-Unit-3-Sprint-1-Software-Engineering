#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30):

    products = []

    for _ in list(range(n)):
        product = Product(name=sample(NOUNS, k=1))

        for i in list(range(randint(5, 101))):
            product.price

        for j in list(range(randint(5, 101))):
            product.weight

        for k in list([x / 10.0 for x in range(0, 25)]):
            product.flammability

        products.append(product)

    return products


def inventory_report(products):

    for product in products:
        unique_products = len(set(products))

    for product in products:
        average_price = (sum(product.price) / len(product.price))

    for product in products:
        average_weight = (sum(product.weight) / len(product.weight))

    for product in products:
        average_flammability = (sum(product.flammability) / len(product.flammability))

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f'Number of Unique Products: {unique_products}')
    print(f'Average Price: {average_price}')
    print(f'Average Weight: {average_weight}')
    print(f'Average Flammability: {average_flammability}')

if __name__ == '__main__':
    inventory_report(generate_products())
