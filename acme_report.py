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
            product.price(product.name[0])

        for j in list(range(randint(5, 101))):
            product.weight(product.name[0])

        for k in list(range(0.0, 2.5)):
            product.flammability(product.name[0])

    products.append(product)

    return products


def inventory_report(products):

    unique_products = []
    average_price = []
    average_weight = []
    average_flammability = []


    for product in products:
        return len(set(products))

    for price in products:
        return sum(price) / len(price)

    for weight in products:
        return sum(weight) / len(weight)

    for flammability in products:
        return sum(flammability) / len(flammability)

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f'Number of Unique Products: {unique_products}')
    print(f'Average Price: {average_price}')
    print(f'Average Weight: {average_weight}')
    print(f'Average Flammability: {average_flammability}')

if __name__ == '__main__':
    inventory_report(generate_products())
