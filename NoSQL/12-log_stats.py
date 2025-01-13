#!/usr/bin/env python3
"""Script for providing Nginx logs stats from MongoDB."""

from pymongo import MongoClient

def log_stats():
   """Provide stats about Nginx logs in MongoDB."""
   client = MongoClient('mongodb://127.0.0.1:27017')
   nginx_collection = client.logs.nginx

   # Total logs
   total_logs = nginx_collection.count_documents({})
   print(f"{total_logs} logs")

   # Methods stats
   methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
   print("Methods:")
   for method in methods:
       count = nginx_collection.count_documents({"method": method})
       print(f"    method {method}: {count}")

   # Status check
   status_check = nginx_collection.count_documents({
       "method": "GET",
       "path": "/status"
   })
   print(f"{status_check} status check")

if __name__ == "__main__":
   log_stats()
