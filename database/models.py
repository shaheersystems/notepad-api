from .db import db


class User(db.Document):
    email=db.StringField(required=True, unique=True)
    password=db.StringField(required=True)
    def check_password(self, password):
        return self.password==password
    

class UserDetails(db.Document):
    name=db.StringField(required=True)
    avatar=db.StringField()
    profession=db.StringField()
    user_id=db.ReferenceField(User)

class Page(db.Document):
    title=db.StringField(required=True)
    content=db.StringField(required=True)
    author=db.ReferenceField(User)
    def to_json(self):
        return {
            "title":self.title,
            "content":self.content,
            "author":self.author
        }
