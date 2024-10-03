from flask import Flask
from flask_restful import Api, Resource

app=Flask(__name__)
api=Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'data':'Hello ,World!'}
    
class GoodbyeWorld(Resource):
    def get(self):
        return {'data':'Goodbye ,World!'}

class User(Resource):
    def __init__(self):
        self.users={
            1:{'name':'Alice'},
            2:{'name':'Bob'},
            
        }
    def get(self, user_id):
        user=self.users.get(user_id, None)
        if user:
            return user
        return {'message':'User not found!'}, 404
    
class Users(Resource):
    def __init__(self):
         self.users={
        1:{'name':'Alice'},
        2:{'name':'Bob'},
        }
    def get(self):
        return self.users
    

api.add_resource(HelloWorld,'/helloworld')
api.add_resource(GoodbyeWorld,'/goodbyeworld')
api.add_resource(User,'/user/<int:user_id>')
api.add_resource(Users,'/users')


if __name__=='__main__':
    app.run(debug=True)
            
        
