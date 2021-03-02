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

@app.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_favorites(user_id):
    all_favs = Favorites.query.all()
    lista_favs = list(map(lambda x: x.serialize_favorite(), all_favs))
    user_favs = list(filter( lambda x: x["user_id"] == user_id , lista_favs))
    favorites = list(map( lambda x: {"fav_id" : x["fav_id"], "favorite" : x["favorite"]}, user_favs))
    result={
        "user_id" : user_id,
        "favorites" : favorites,
    }
    return jsonify(result), 200

@app.route('/users/<int:user_id>/favorites', methods=['POST'])
def add_favorite(user_id):
    user = User.query.get(user_id)
    if user is None:
        raise APIException('This user is not in the database', status_code=404)

    all_peoples = Character.query.all()
    people = list(map(lambda x: x.serialize_character(), all_peoples))

    all_planets = Planet.query.all()
    planets = list(map(lambda x: x.serialize_planet(), all_planets))

    # recibir info del request
    request_body = request.get_json()
    fav = Favorites.verification("algo", request_body["fav_name"], planets, people)
    favorito = Favorites(user_id = user_id, favorite = fav)
    db.session.add(favorito)
    db.session.commit()

    return jsonify("Favorite added"), 200

@app.route('/favorites/<int:fav_id>', methods=['DELETE'])
def del_favorite(fav_id):
    
    fav = Favorites.query.get(fav_id)
    if fav is None:
        raise APIException('Favorite not found', status_code=404)

    db.session.delete(fav)
    db.session.commit()

    return jsonify({"msg": "Favorite deleted" }), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
