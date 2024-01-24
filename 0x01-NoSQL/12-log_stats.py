#!/usr/bin/env python3
"""Python script that provides some stats
about Nginx logs stored in MongoDB"""
import pymongo

if __name__ == "__main__":
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    mydb = myclient.logs
    mycol = mydb.nginx

    print("{} logs".format(len(mycol.find())))
    print("Methods:".format(len(mycol.find())))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for m in methods:
        print("\tmethod {}: {}".format(m, len(mycol.find({"method": m}))))

    print("{} status check".format(
        len(mycol.find({"method": "GET", "path": "/status"}))))
