#!/usr/bin/env python3
"""
Python script that provides some stats
about Nginx logs stored in MongoDB
"""

import pymongo
from collections import Counter

if __name__ == "__main__":
    myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    mydb = myclient.logs
    mycol = mydb.nginx

    print("{} logs".format(mycol.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for m in methods:
        print("\tmethod {}: {}".format(m, mycol.count_documents({"method": m})))

    print("{} status check".format(
        mycol.count_documents({"method": "GET", "path": "/status"})))
    print("IPs:")

    mydocs = mycol.find()
    counting_dict = sorted(
        Counter(one['ip'] for one in mydocs).items(),
        key=lambda one: one[1],
        reverse=True
    )
    i = 1

    for ip in counting_dict:
        print(f"\t{ip}: {counting_dict[ip]}")
        if i == 10:
            break
        i += 1
