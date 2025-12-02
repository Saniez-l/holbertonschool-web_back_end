#!/usr/bin/env python3
"""
Docstring for NoSQL.10-update_topics
Python function that changes all topics of
a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Docstring for update_topics
    function that changes all topics of a school document

    :param mongo_collection: Description
    :param name: Description
    :param topics: Description
    """
    query = {"name": name}
    new_value = {"$set": {"topics": topics}}

    return mongo_collection.update_many(query, new_value)
