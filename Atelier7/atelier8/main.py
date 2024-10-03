from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videos.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
auth = HTTPTokenAuth(scheme='Bearer')
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    likes = db.Column(db.Integer, default=0)
    views = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f"Video(name = {self.name}, description = {self.description}, likes = {self.likes}, views = {self.views})"
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("description", type=str, help="Description of the video is required", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video")
video_update_args.add_argument("description", type=str, help="Description of the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'likes': fields.Integer,
    'views': fields.Integer
}
def abort_if_video_id_doesnt_exist(video_id):
    if not VideoModel.query.get(video_id):
        abort(404, message=f"Video ID {video_id} doesn't exist")

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return VideoModel.query.get(video_id)
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], description=args['description'])
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        video = VideoModel.query.get(video_id)
        if not video:
            abort(404, message="Video doesn't exist, cannot update")
        if args['name']:
            video.name = args['name']
        if args['description']:
            video.description = args['description']
        db.session.commit()
        return video
    
    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        video = VideoModel.query.get(video_id)
        db.session.delete(video)
        db.session.commit()
        return '', 204
api.add_resource(Video, "/video/<int:video_id>")
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
