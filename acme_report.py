#!/usr/bin/env python

from random import randint, sample, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30):

    products = []

    for _ in range(n):
        name = choice(ADJECTIVES) + " " + choice(NOUNS)
        price = randint(5, 101)
        weight = randint(5, 101)
        flammability = uniform(0, 2.5)

        products.append(Product(name=name, price=price, weight=weight,
                                flammability=flammability))
        """
        product = Product(name=sample(NOUNS, k=1))

        for i in list(range(randint(5, 101))):
            product.price

        for j in list(range(randint(5, 101))):
            product.weight

        for k in list([x / 10.0 for x in range(0, 25)]):
            product.flammability

        products.append(product)
        """

    return products

def inventory_report(products):

    unique_products = []
    average_price = 0
    average_weight = 0
    average_flammability = 0

    for product in products:
        unique_products.append(len(set(products)))
        average_price += product.price
        average_weight += product.weight
        average_flammability += product.flammability
    average_price = average_price / 30
    average_weight = average_weight / 30
    average_flammability = average_flammability / 30

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f'Number of Unique Products: {unique_products[0]}')
    print(f'Average Price: {average_price}')
    print(f'Average Weight: {average_weight}')
    print(f'Average Flammability: {average_flammability}')

if __name__ == '__main__':
    inventory_report(generate_products())
