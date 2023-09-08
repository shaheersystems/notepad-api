from flask import Flask, jsonify, request, render_template
from flask_restful import Api
from database import db
from resources import routes
app = Flask(__name__)

db_name="notepad_db"

app.config['MONGODB_SETTINGS'] = {
    "host": "mongodb://localhost:27017/"+db_name
}

api = Api(app)
db.initiallize_db(app)
routes.initialize_routes(api)


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
