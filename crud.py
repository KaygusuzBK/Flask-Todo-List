from flask import Flask, jsonify, request, json
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get_all', methods=['GET'])
def get_all():
    products = mongo.db.products
    output = []
    for q in products.find():
        output.append({'name' : q['name'], 'price' : q['price']})
    return jsonify({'result' : output})

@app.route('/get/<name>', methods=['GET'])
def get_one(name):
    products = mongo.db.products
    q = products.find_one({'name' : name})
    if q:
        output = {'name' : q['name'], 'price' : q['price']}
    else:
        output = 'No results found'
    return jsonify({'result' : output})

@app.route('/add', methods=['POST'])
def add_one():
    products = mongo.db.products
    name = request.json['name']
    price = request.json['price']
    product_id = products.insert({'name': name, 'price': price})
    new_product = products.find_one({'_id': product_id })
    output = {'name' : new_product['name'], 'price' : new_product['price']}
    return jsonify({'result' : output})

@app.route('/update/<name>', methods=['PUT'])
def update_one(name):
    products = mongo.db.products
    price = request.json['price']
    product = products.find_one({'name': name})
    if product:
        product['price'] = price
        products.save(product)
        output = {'name' : product['name'], 'price' : product['price']}
    else:
        output = 'No results found'
    return jsonify({'result' : output})

@app.route('/delete/<name>', methods=['DELETE'])
def delete_one(name):
    products = mongo.db.products
    product = products.find_one({'name': name})
    if product:
        products.remove(product)
        output = 'Product deleted'
    else:
        output = 'No results found'
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)
