#!/usr/bin/env python3
"""List all documents in Python """
import pymongo


def top_students(mongo_collection):
    """averageScore"""
    return mongo_collection.find().sort("averageScore")
