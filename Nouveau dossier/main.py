# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_httpauth import HTTPTokenAuth

# Cr�er une instance de l'application Flask
app = Flask(__name__)
api = Api(app)

# Initialiser l'authentification par jetons
auth = HTTPTokenAuth(scheme='Bearer')

# Dictionnaire pour stocker les �tudiants
students = {}

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

# Configurer le parser pour les arguments PUT
student_put_args = reqparse.RequestParser()
student_put_args.add_argument("name", type=str, help="Name of the student is required", required=True)
student_put_args.add_argument("age", type=int, help="Age of the student", required=True)
student_put_args.add_argument("grade", type=float, help="Grade of the student", required=True)

# Fonction pour g�rer les erreurs si l'ID de l'�tudiant n'existe pas
def abort_if_student_id_doesnt_exist(student_id):
    if student_id not in students:
        abort(404, message="Could not find student.")

# Fonction pour g�rer les erreurs si l'�tudiant existe d�j�
def abort_if_student_exists(student_id):
    if student_id in students:
        abort(409, message="Student already exists with that ID")

# Classe pour la ressource �tudiant
class Student(Resource):
    @auth.login_required
    def get(self, student_id):
        abort_if_student_id_doesnt_exist(student_id)
        return students[student_id]

    @auth.login_required
    def put(self, student_id):
        abort_if_student_exists(student_id)
        args = student_put_args.parse_args()
        students[student_id] = args
        return students[student_id], 201

    @auth.login_required
    def delete(self, student_id):
        abort_if_student_id_doesnt_exist(student_id)
        del students[student_id]
        return '', 204

# Ajouter la ressource Student � l'API
api.add_resource(Student, "/student/<int:student_id>")

# D�marrer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
