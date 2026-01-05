#!/usr/bin/env python3
"""
Docstring for NoSQL.8-all
Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Docstring for list_all
    :param mongo_collection: Lists all documents in a collection.
    """
    return list(mongo_collection.find())
