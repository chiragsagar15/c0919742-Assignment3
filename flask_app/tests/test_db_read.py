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

def test_mongodb_connection():
    client = MongoClient(connection_string)
    response = client.admin.command('ping')
    assert response['ok'] == 1.0
