from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
 
# Créer une instance de l'application Flask
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db = SQLAlchemy(app)


class CarModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make= db.Column(db.String(100), nullable=False)
    model= db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
 
    def __repr__(self):
        return f"car(make = {make}, model = {model}, year = {year},price = {price})"
    
    # Arguments pour les requêtes PUT
car_put_args = reqparse.RequestParser()
car_put_args.add_argument("make", type=str, help="make of the car is required", required=True)
car_put_args.add_argument("model", type=str, help="model of the car is required", required=True)
car_put_args.add_argument("year", type=str, help="year of the car is required", required=True)
car_put_args.add_argument("price", type=int, help="price of the car is required", required=True)
 
# Arguments pour les requêtes PATCH
car_update_args = reqparse.RequestParser()
car_update_args.add_argument("make", type=str, help="make of the car")
car_update_args.add_argument("model", type=str, help="model of the car")
car_update_args.add_argument("year", type=str, help="year of the car")
car_update_args.add_argument("price", type=int, help="price of the car")
 
# Champs de ressource pour la sérialisation
resource_fields = {
    'id': fields.Integer,
    'make': fields.String,
    'model':fields.String,
    'year': fields.String,
    'price': fields.Integer
}
# Fonction pour arrêter si l'ID du cours n'existe pas
def abort_if_car_id_doesnt_exist(car_id):
    if not CarModel.query.get(car_id):
        abort(404, message=f"car ID {car_id} doesn't exist")
 
# Classe de ressource pour les opérations CRUD sur les cours
class car(Resource):
    
    @marshal_with(resource_fields)
    def get(self, car_id):
        result = CarModel.query.filter_by(id=car_id).first()
        if not result:
            abort(404, message="Could not find car with that id")
        return result
 
    @marshal_with(resource_fields)
    def put(self, car_id):
        args = car_put_args.parse_args()
        result = CarModel.query.filter_by(id=car_id).first()
        if result:
            abort(409, message="car id taken...")
 
        car = CarModel(id=car_id, make=args['make'], model=args['model'],year=args['year'], price=args['price'])
        db.session.add(car)
        db.session.commit()
        return car, 201
    
    @marshal_with(resource_fields)
    
    def patch(self, car_id):
        args = car_update_args.parse_args()
        result = CarModel.query.filter_by(id=car_id).first()
        if not result:
            abort(404, message="car doesn't exist, cannot update")
    
        if args['make']:
            result.make = args['make']
        if args['model']:
            result.model = args['model']
        if args['year']:
            result.year = args['year']
        if args['price']:
            result.price = args['price']
    
        db.session.commit()
        return result
 
    def delete(self, car_id):
        result = CarModel.query.filter_by(id=car_id).first()
        if not result:
            abort(404, message="car doesn't exist, cannot delete")
    
        db.session.delete(result)
        db.session.commit()
        return '', 204
    
    # Ajouter la ressource car à l'API
api.add_resource(car, "/car/<int:car_id>")


# Démarrer le serveur Flask
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
 