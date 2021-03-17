from flask_restful import abort, Resource
from flask import jsonify
from data import db_session
from data.news import User
from data.reqparse_user import parser
from werkzeug.security import generate_password_hash


def abort_if_user_not_found(news_id):
    session = db_session.create_session()
    users = session.query(User).get(news_id)
    if not users:
        abort(404, message=f"User {news_id} not found")


def set_password(self, password):
    self.hashed_password = generate_password_hash(password)


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({"user": user.to_dict(
            only=("name", "about", "email", "created_date", "hashed_password"))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({"success": "OK"})


class NewListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({"user": [item.to_dict(
            only=("name", "about", "email", "created_date", "hashed_password")) for item in users]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args["name"],
            about=args["about"],
            email=args["email"],
            created_date=args["created_date"],
            hashed_password=args["hashed_password"],
        )
        session.add(user)
