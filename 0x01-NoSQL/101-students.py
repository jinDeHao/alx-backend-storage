#!/usr/bin/env python3
"""List all documents in Python """
import pymongo


def top_students(mongo_collection):
    """averageScore"""
    stus = mongo_collection.find()
    average = {}
    for s in stus:
        sum = 0
        for t in s["topics"]:
            sum += t["score"]
        average[s["name"]] = sum / len(s["topics"])
    return average
