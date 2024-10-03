from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
 
# Créer une instance de l'application Flask
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
db = SQLAlchemy(app)
 
# Modèle de données pour les cours
class CourseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
 
    def __repr__(self):
        return f"Course(name = {name}, description = {description}, duration = {duration})"
 
# Arguments pour les requêtes PUT
course_put_args = reqparse.RequestParser()
course_put_args.add_argument("name", type=str, help="Name of the course is required", required=True)
course_put_args.add_argument("description", type=str, help="Description of the course is required", required=True)
course_put_args.add_argument("duration", type=int, help="Duration of the course is required", required=True)
 
# Arguments pour les requêtes PATCH
course_update_args = reqparse.RequestParser()
course_update_args.add_argument("name", type=str, help="Name of the course")
course_update_args.add_argument("description", type=str, help="Description of the course")
course_update_args.add_argument("duration", type=int, help="Duration of the course")
 
# Champs de ressource pour la sérialisation
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'duration': fields.Integer
}
# Fonction pour arrêter si l'ID du cours n'existe pas
def abort_if_course_id_doesnt_exist(course_id):
    if not CourseModel.query.get(course_id):
        abort(404, message=f"Course ID {course_id} doesn't exist")
 
# Classe de ressource pour les opérations CRUD sur les cours
class Course(Resource):
    
    @marshal_with(resource_fields)
    def get(self, course_id):
        result = CourseModel.query.filter_by(id=course_id).first()
        if not result:
            abort(404, message="Could not find course with that id")
        return result
 
    @marshal_with(resource_fields)
    def put(self, course_id):
        args = course_put_args.parse_args()
        result = CourseModel.query.filter_by(id=course_id).first()
        if result:
            abort(409, message="Course id taken...")
 
        course = CourseModel(id=course_id, name=args['name'], description=args['description'], duration=args['duration'])
        db.session.add(course)
        db.session.commit()
        return course, 201
    
    @marshal_with(resource_fields)
    
    def patch(self, course_id):
        args = course_update_args.parse_args()
        result = CourseModel.query.filter_by(id=course_id).first()
        if not result:
            abort(404, message="Course doesn't exist, cannot update")
    
        if args['name']:
            result.name = args['name']
        if args['description']:
            result.description = args['description']
        if args['duration']:
            result.duration = args['duration']
    
        db.session.commit()
        return result
 
    def delete(self, course_id):
        result = CourseModel.query.filter_by(id=course_id).first()
        if not result:
            abort(404, message="Course doesn't exist, cannot delete")
    
        db.session.delete(result)
        db.session.commit()
        return '', 204
    
    # Ajouter la ressource Course à l'API
api.add_resource(Course, "/course/<int:course_id>")



# Démarrer le serveur Flask
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)