#!/usr/bin/env python3
"""
Docstring for NoSQL.9-insert_school
Python function that inserts a new document in
a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Docstring for function that inserts a new document in a collection

    :param mongo_collection: Description
    :param kwargs: Description
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
