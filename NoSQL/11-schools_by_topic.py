#!/usr/bin/env python3
"""
Docstring for NoSQL.11-schools_by_topic
Python function that returns the list of
school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    cursor = mongo_collection.find({"topic": topic})
    document = list(cursor)
    return document
