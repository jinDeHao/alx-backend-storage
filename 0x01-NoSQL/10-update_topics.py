#!/usr/bin/env python3
"""update topics where the name == name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """update topics where the name == name"""
    return mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}},
    )
