#!/usr/bin/env python3
"""Nginx logs stats from MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
   client = MongoClient('mongodb://127.0.0.1:27017')
   db = client.logs
   nginx = db.nginx

   print(f"{nginx.count_documents({})} logs")
   print("Methods:")
   methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
   for method in methods:
       print(f"    method {method}: {nginx.count_documents({'method': method})}")
   print(f"{nginx.count_documents({'method': 'GET', 'path': '/status'})} status check")