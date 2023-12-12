from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Pong!"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message": "products list"})

@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productsFound = [product for product in products if product.get('name') == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    
    return jsonify({"message": "product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    print(request.json)
    new_product = {
        "name": request.json.get('name'),
        "price": request.json.get('price'),
        "quantity": request.json.get('quantity')
    }
    products.append(new_product)
    return jsonify({"message": "product added succesfully", "produc": products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product.get('name') == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json.get('name')
        productsFound[0]['price'] = request.json.get('price')
        productsFound[0]['quantity'] = request.json.get('quantity')
        return jsonify({
            "message": "product updated",
            "product": productsFound[0]
        })
    
    return jsonify({"message": "product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product.get('name') == product_name]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({
            "message": "product deleted",
            "product": products
        })

    return jsonify({"message": "product not found"})


if __name__ == '__main__':
    app.run(debug=True, port=8000)



