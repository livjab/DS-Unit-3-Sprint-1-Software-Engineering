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
        flammability = [x / 10.0 for x in range(0, 25)]

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
    average_price = []
    average_weight = []
    average_flammability = []

    for product in products:
        unique_products.append(len(set(products)))

    #for product in products:
    #    average_price.append(sum(product.price) / len(product.price))

    #for product in products:
    #    average_weight.append(sum(product.weight) / len(product.weight))

    #for product in products:
    #    average_flammability.append(sum(product.flammability) / len(product.flammability))


    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f'Number of Unique Products: {unique_products[0]}')
    #print(f'Average Price: {average_price[0]}')
    #print(f'Average Weight: {average_weight[0]}')
    #print(f'Average Flammability: {average_flammability[0]}')

if __name__ == '__main__':
    inventory_report(generate_products())
