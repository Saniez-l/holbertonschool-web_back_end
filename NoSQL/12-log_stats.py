#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":

    """commande pour adresse clien mongo db: sudo ss -tlnp | grep mongod"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    """nombre total de log"""
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    """comter par methode"""
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    """cherche les documents qui ont A LA FOIS method=GET et path=/status"""
    status_check_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check")
