#!/usr/bin/env python3
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["logs"]
mycol = mydb["nginx"]

print("{} logs".format(len(mycol.find())))
print("Methods:".format(len(mycol.find())))
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


for m in methods:
    print("\tmethod {}: {}".format(m, len(mycol.find({"method": m}))))

print("{} status check".format(
    len(mycol.find({"method": "GET", "path": "/status"}))))
