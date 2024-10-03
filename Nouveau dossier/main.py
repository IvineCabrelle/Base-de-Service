# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_httpauth import HTTPTokenAuth

# Créer une instance de l'application Flask
app = Flask(__name__)
api = Api(app)

# Initialiser l'authentification par jetons
auth = HTTPTokenAuth(scheme='Bearer')

# Dictionnaire pour stocker les étudiants
students = {}

# Liste des jetons d'authentification (dans un cas réel, ces jetons devraient être stockés de manière sécurisée)
tokens = {
    "secrettoken123": "user1",
    "anothersecrettoken456": "user2"
}

# Fonction pour vérifier les jetons
@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]

# Configurer le parser pour les arguments PUT
student_put_args = reqparse.RequestParser()
student_put_args.add_argument("name", type=str, help="Name of the student is required", required=True)
student_put_args.add_argument("age", type=int, help="Age of the student", required=True)
student_put_args.add_argument("grade", type=float, help="Grade of the student", required=True)

# Fonction pour gérer les erreurs si l'ID de l'étudiant n'existe pas
def abort_if_student_id_doesnt_exist(student_id):
    if student_id not in students:
        abort(404, message="Could not find student.")

# Fonction pour gérer les erreurs si l'étudiant existe déjà
def abort_if_student_exists(student_id):
    if student_id in students:
        abort(409, message="Student already exists with that ID")

# Classe pour la ressource Étudiant
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

# Ajouter la ressource Student à l'API
api.add_resource(Student, "/student/<int:student_id>")

# Démarrer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)
