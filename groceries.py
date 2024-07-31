#!/usr/bin/env python3

import sys
import doctest

"""
Stanford CS106A Section Problem
Written by Elyse Cornwall
"""

def add_item(groceries, store, item, num):
    """
    Given a groceries dict which may
    already contain some data, update the
    dict to add new data for the given
    store, item, and num of that item.
    >>> add_item({}, 'safeway', 'eggs', 1) # new store, new item
    {'safeway': {'eggs': 1}}
    >>> add_item({'safeway': {'eggs': 1}}, 'costco', 'croissant', 12) # new store, new item
    {'safeway': {'eggs': 1}, 'costco': {'croissant': 12}}
    >>> add_item({'safeway': {'eggs': 1}, 'costco': {'croissant': 12}}, 'safeway', 'eggs', 2) # seen store, seen item
    {'safeway': {'eggs': 3}, 'costco': {'croissant': 12}}
    >>> add_item({'safeway': {'eggs': 3}, 'costco': {'croissant': 12}}, 'safeway', 'coconut milk', 3) # seen store, new item
    {'safeway': {'eggs': 3, 'coconut milk': 3}, 'costco': {'croissant': 12}}
    """
    if store not in groceries:
        # YOUR ONE LINE HERE
        groceries[store] = {}

    inner = groceries[store] # access inner dict for store
    if item not in inner:
        # YOUR ONE LINE HERE
        # for store, value in groceries.items():
        inner[item] = num
    # YOUR ONE LINE HERE
    
    return groceries

doctest.testmod(name='add_item')


def make_groceries(filename):
    """
    Given a grocery list file, where each
    line is in the format 'store:item,num'
    create and return the groceries dict
    made from this list.
    Hint: Use your helper function!
    >>> make_groceries('short_list.txt')
    {'safeway': {'eggs': 3, 'coconut milk': 3}, 'costco': {'croissant': 12}}
    """
    groceries = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            # YOUR CODE HERE
    return groceries


def print_groceries(groceries):
    """
    (provided)
    Prints contents of groceries dict.
    """
    for store in groceries:
        items = groceries[store]
        for item in items:
            count = items[item]
            print('You need ' + str(count) + ' ' + item + '(s) from ' + store)


def main():
    args = sys.argv[1:]
    # to run from terminal:
    # python3 groceries.py filename      # prints out all groceries
    if len(args) == 1:
        groceries = make_groceries(args[0])
        print_groceries(groceries)


if __name__ == '__main__':
    main()
