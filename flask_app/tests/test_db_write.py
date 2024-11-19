# Chirag Tarsemlal Sagar.

from pymongo import MongoClient
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from urllib.parse import quote_plus
load_dotenv()
username = quote_plus(os.getenv('MONGODB_USERNAME')) 
password = quote_plus(os.getenv('MONGODB_PASSWORD'))

connection_string = f"mongodb+srv://{username}:{password}@mystoredb.qodsv.mongodb.net/shop_db?retryWrites=true&w=majority&appName=mystoredb"


def test_mongodb_write_operation():
    client = MongoClient(connection_string)
    db = client['shop_db']
    products_collection = db['products']

    test_product = {
        "name": "Test Watch",
        "price": 99.99,
        "tag": "Test Watch",
        "image_path": "images/smartwatch.jpg" 
    }
    result = products_collection.insert_one(test_product)

    inserted_product = products_collection.find_one({"_id": result.inserted_id})
    assert inserted_product['name'] == "Test Watch"
    assert inserted_product['price'] == 99.99
    assert inserted_product['tag'] == "Test Watch"
    assert inserted_product['image_path'] == "images/smartwatch.jpg"

    products_collection.delete_one({"_id": result.inserted_id})

    deleted_product = products_collection.find_one({"_id": result.inserted_id})
    assert deleted_product is None
