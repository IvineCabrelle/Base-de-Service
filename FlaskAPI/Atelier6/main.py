from flask import Flask, jsonify
from flask_restful import Api,Resource
from flask_jwt_extended import JWTManager
from flask_restful import reqparse



app = Flask(__name__)
api = Api(app)


jwt = JWTManager(app)
products = {}



parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='Name of the product')
parser.add_argument('price', type=float, required=True, help='Price of the product')
def product_not_found(name):
    return jsonify({'message': f'Product {name} not found'}), 404

def product_already_exists(name):
    return jsonify({'message': f'Product {name} already exists'}), 400

class Product(Resource):
    def get(self, name):
        if name in products:
            return products[name]
        else:
            return product_not_found(name)

    def put(self, name):
        if name in products:
            return product_already_exists(name)
        args = parser.parse_args()
        products[name] = {'price': args['price']}
        return products[name], 201

    def delete(self, name):
        if name in products:
            del products[name]
            return '', 204
        else:
            return product_not_found(name)
     
api.add_resource(Product, '/product/<string:name>')
if __name__ == '__main__':
    app.run(debug=True)


