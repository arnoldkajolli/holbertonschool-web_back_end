#!/usr/bin/env python3
"""Function to insert a new document in MongoDB."""

def insert_school(mongo_collection, **kwargs):
   """Insert new document in collection with kwargs and return _id."""
   result = mongo_collection.insert_one(kwargs)
   return result.inserted_id