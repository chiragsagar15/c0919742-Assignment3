from pymongo import MongoClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import connection_string

def test_mongodb_write_operation():
    client = MongoClient(connection_string)
    db = client['shop_db']
    products_collection = db['products']

    test_product = {"name": "Test Watch", "price": 99.99, "tag": "Test Watch"}
    result = products_collection.insert_one(test_product)

    inserted_product = products_collection.find_one({"_id": result.inserted_id})
    assert inserted_product['name'] == "Test Watch"

    products_collection.delete_one({"_id": result.inserted_id})
