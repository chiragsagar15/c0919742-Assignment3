import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pymongo import MongoClient
from app import connection_string

def test_mongodb_connection():
    client = MongoClient(connection_string)
    response = client.admin.command('ping')
    assert response['ok'] == 1.0