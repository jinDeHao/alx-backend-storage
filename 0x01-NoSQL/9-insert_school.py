#!/usr/bin/env python3
"""List all documents in Python """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """List all documents in Python """
    return mongo_collection.insert_one(kwargs).inserted_id
