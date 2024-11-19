import sys
import os
import time
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import connection_string  # Make sure 'connection_string' is defined properly in 'app'

# Add parent directory to sys.path to ensure proper import of 'app'


def test_mongodb_connection():
    retries = 3
    for attempt in range(retries):
        try:
            client = MongoClient(connection_string)
            # Ping the server to check if it's up
            response = client.admin.command('ping')
            assert response['ok'] == 1.0
            print("MongoDB connection successful!")
            return  # Test passes if connection is successful
        except ConnectionFailure as e:
            if attempt < retries - 1:
                print(f"Attempt {attempt + 1} failed, retrying in 2 seconds...")
                time.sleep(2)  # Wait before retrying
            else:
                assert False, f"MongoDB connection failed after {retries} attempts: {e}"

