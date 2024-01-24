#!/usr/bin/env python3
"""List all documents in Python """
import pymongo


def list_all(mongo_collection) -> list:
    """List all documents in Python """
    return mongo_collection.find()
