from flask import request, Response, jsonify
from flask_restful import Resource

from database.models import User, Page, UserDetails


class RegisterApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body).save()
        id = user.id
        return {'id': str(id)}, 200
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)
    

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': 'Email or password invalid'}, 401
        return {'token': str(user.id)}, 200
    
class UserDetailsApi(Resource):
    def post(self):
        body = request.get_json()
        """
        {
            "name": "Rahul",
            "avatar": "https://www.google.com",
            "profession": "Software Engineer",
            "user_id": "5f9a3c6d3c9e7b7d1e8b8d4b"
        }
        """
        user_details = UserDetails(**body).save()
        id = user_details.id
        return {'id': str(id)}, 200
class DetailsApi(Resource):
    def get(self, user_id):
        user_details = UserDetails.objects.get(user_id=user_id)
        return jsonify(user_details)

class PagesApi(Resource):
    def post(self):
        body = request.get_json()
        """
        {
            "title": "About Me",
            "content": "I am a Software Engineer",
            "author": "5f9a3c6d3c9e7b7d1e8b8d4b"
        }
        """
        page = Page(**body).save()
        id = page.id
        return {'id': str(id)}, 200
    def get(self):
        user_id = request.args.get('author')
        pages = Page.objects.get(author=user_id)
        return jsonify(pages)
    

class SinglePageApi(Resource):
    def get(self, page_id):
        page = Page.objects.get(id=page_id)
        return jsonify(page)
    def put(self, page_id):
        body = request.get_json()
        Page.objects.get(id=page_id).update(**body)
        return jsonify({"message": "Page updated successfully."}), 200
    def delete(self, page_id):
        page = Page.objects.get(id=page_id).delete()
        return jsonify({"message": "Page deleted successfully."}), 200
    