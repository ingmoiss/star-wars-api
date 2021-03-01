"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    result = list(map(lambda x: x.serialize_user(), users))

    return jsonify(result), 200

#Get a single user by id
@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)

    if user is None:
        raise APIException('The user is not registered', status_code=404)

    result = user.serialize_user()

    return jsonify(result), 200

@app.route('/planets', methods=['GET'])
def get_planets():

    planets = Planet.query.all()

    result = list(map(lambda x : x.serialize_planet(), planets))

    return jsonify(result), 200

#Get a single planet by id
@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    
    planet =  Planet.query.get(planet_id)
    if planet is None:
        raise APIException('The planet is not registered', status_code=404)
    result = planet.serialize_planet()

    return jsonify(result), 200

@app.route('/peoples', methods=['GET'])
def get_peoples():

    peoples = Character.query.all()

    result = list(map(lambda x : x.serialize_character(), peoples))

    return jsonify(result), 200

#Get a single planet by id
@app.route('/people/<int:people_id>', methods=['GET'])
def get_people(people_id):
    
    people =  Character.query.get(people_id)

    if people is None:
        raise APIException('The planet is not registered', status_code=404)
    result = people.serialize_character()

    return jsonify(result), 200



    

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
