# Chirag Tarsemlal Sagar.

from pymongo import MongoClient
from urllib.parse import quote_plus
from flask import Flask, render_template
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialising the Flask Application
app = Flask(__name__)

# Encoding username and password for MongoDB connection
username = quote_plus(os.getenv('MONGODB_USERNAME')) 
password = quote_plus(os.getenv('MONGODB_PASSWORD'))


# Connection string for MongoDB Atlas
connection_string = f"mongodb+srv://{username}:{password}@mystoredb.qodsv.mongodb.net/shop_db?retryWrites=true&w=majority&appName=mystoredb"

# Creating MongoDB client and connecting to the database
client = MongoClient(connection_string)

# Accessing the 'shop_db' database and 'products' collection from the MongoDB Cluster
db = client['shop_db']
products_collection = db['products']

# Defining route for Home Page & for displaying products on the Products Page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    products = products_collection.find()
    return render_template('products.html', products=products)

# Running the Flask Application
if __name__ == '__main__':
    app.run(debug=True)
