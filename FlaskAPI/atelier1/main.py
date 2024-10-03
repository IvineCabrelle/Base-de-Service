from flask import Flask
from flask_restful import Api, Resource

#créer une instance de l'application flask
app=Flask(__name__)

#creer une instance de l'api restful
api=Api(app)
#definir une ressource simple

class HelloWord (Resource):
    
    def get(self):
        return {'message':'Hello, Word'}

#Ajouter la ressource a l'api

api.add_resource(HelloWord,'/')


#class GoodByeWorld(Resource):
    #def get(self):
        #return {'message':'GoodBye, Word'}

#api.add_resource(GoodByeWorld,'/goodBye')
    

#Demarrer le serveur Flask

if __name__=='__main__':
    app.run(debug=True)