# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth

# Cr�er une instance de l'application Flask
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)

# Initialiser l'authentification par jetons
auth = HTTPTokenAuth(scheme='Bearer')

# Liste des jetons d'authentification (dans un cas r�el, ces jetons devraient �tre stock�s de mani�re s�curis�e)
tokens = {
    "secrettoken123": "user1",
    "anothersecrettoken456": "user2"
}

# Fonction pour v�rifier les jetons
@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

# Mod�le de donn�es pour les commandes
class OrderModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Order(product_name = {product_name}, quantity = {quantity}, price = {price}, order_date = {order_date})"

# Arguments pour les requ�tes PUT
order_put_args = reqparse.RequestParser()
order_put_args.add_argument("product_name", type=str, help="Name of the product is required", required=True)
order_put_args.add_argument("quantity", type=int, help="Quantity of the product is required", required=True)
order_put_args.add_argument("price", type=float, help="Price of the product is required", required=True)
order_put_args.add_argument("order_date", type=str, help="Order date is required", required=True)

# Arguments pour les requ�tes PATCH
order_update_args = reqparse.RequestParser()
order_update_args.add_argument("product_name", type=str, help="Name of the product")
order_update_args.add_argument("quantity", type=int, help="Quantity of the product")
order_update_args.add_argument("price", type=float, help="Price of the product")
order_update_args.add_argument("order_date", type=str, help="Order date")

# Champs de ressource pour la s�rialisation
resource_fields = {
    'id': fields.Integer,
    'product_name': fields.String,
    'quantity': fields.Integer,
    'price': fields.Float,
    'order_date': fields.String
}

# Fonction pour arr�ter si l'ID de la commande n'existe pas
def abort_if_order_id_doesnt_exist(order_id):
    if not OrderModel.query.get(order_id):
        abort(404, message=f"Order ID {order_id} doesn't exist")

# Classe de ressource pour les op�rations CRUD sur les commandes
class Order(Resource):
    @auth.login_required
    @marshal_with(resource_fields)
    def get(self, order_id):
        result = OrderModel.query.filter_by(id=order_id).first()
        if not result:
            abort(404, message="Could not find order with that id")
        return result

    @auth.login_required
    @marshal_with(resource_fields)
    def put(self, order_id):
        args = order_put_args.parse_args()
        result = OrderModel.query.filter_by(id=order_id).first()
        if result:
            abort(409, message="Order id taken...")

        order = OrderModel(id=order_id, product_name=args['product_name'], quantity=args['quantity'], price=args['price'], order_date=args['order_date'])
        db.session.add(order)
        db.session.commit()
        return order, 201

    @auth.login_required
    @marshal_with(resource_fields)
    def patch(self, order_id):
        args = order_update_args.parse_args()
        result = OrderModel.query.filter_by(id=order_id).first()
        if not result:
            abort(404, message="Order doesn't exist, cannot update")

        if args['product_name']:
            result.product_name = args['product_name']
        if args['quantity']:
            result.quantity = args['quantity']
        if args['price']:
            result.price = args['price']
        if args['order_date']:
            result.order_date = args['order_date']

        db.session.commit()
        return result

    @auth.login_required
    def delete(self, order_id):
        result = OrderModel.query.filter_by(id=order_id).first()
        if not result:
            abort(404, message="Order doesn't exist, cannot delete")

        db.session.delete(result)
        db.session.commit()
        return '', 204

# Ajouter la ressource order � l'API
api.add_resource(Order, "/order/<int:order_id>")

# D�marrer le serveur Flask
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
