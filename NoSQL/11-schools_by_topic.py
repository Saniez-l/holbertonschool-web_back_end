#!/usr/bin/env python3
"""
Docstring for NoSQL.11-schools_by_topic
Python function that returns the list of
school having a specific topic
"""


def schools_by_topic(mongo_collection, topics):
    """
    Docstring for schools_by_topic
    function that returns the list of
    function that returns the list of
    school

    :param mongo_collection: Description
    :param topics: Description
    """
    cursor = mongo_collection.find({"topics": topics})
    document = list(cursor)
    return document
