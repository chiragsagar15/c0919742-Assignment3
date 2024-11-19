# Chirag Tarsemlal Sagar.

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app


def test_products_route_invalid_method():
    with app.test_client() as client:
        response = client.post('/products')
        assert response.status_code == 405
