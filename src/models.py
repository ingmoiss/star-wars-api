from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(300), unique = True, nullable=False)
    password = db.Column(db.String(300), unique=False, nullable=False)
    email = db.Column(db.String(300), unique = True, nullable=False)
    first_name = db.Column(db.String(300), unique=False, nullable=False)
    last_name = db.Column(db.String(40), unique=False, nullable=False)
    favorites = db.relationship('Favorites', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.id

    #The information is serialized
    def serialize_user(self):
        return {
            "id": self.id,
            "nickname" : self.nickname,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = 'character'
    character_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(300), unique=True, nullable=False)
    birth = db.Column(db.String(300), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    height = db.Column(db.Integer, nullable=False) 
    skin_color = db.Column(db.String(300), nullable=False)
    eye_color = db.Column(db.String(300), nullable=False)
    hair_color = db.Column(db.String(300), nullable=False)
    mass = db.Column(db.Integer, nullable=False) 
    edited = db.Column(db.String(300), nullable=False)
    created = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(300), unique=True, nullable=False)

    def __repr__(self):
        return '<Character %r>' % self.user_id

    #The information is serialized
    def serialize_character(self):
        return {
            "character_id": self.character_id,
            "name" : self.name,
            "birth" : self.birth,
            "gender" : self.gender,
            "height": self.height,
            "skin_color": self.skin_color,
            "eye_color" : self.eye_color,
            "hair_color" : self.hair_color,
            "mass" : self.mass,
            "edited": self.edited,
            "created": self.created,
            "url" : self.url,
        }


class Planet(db.Model):
    __tablename__ = 'planet'
    planet_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(300), nullable=False)
    orbital_period = db.Column(db.String(300), nullable=False)
    rotation_period = db.Column(db.String(300), nullable=False)
    diameter = db.Column(db.String(300), nullable=False)
    gravity = db.Column(db.String(300), nullable=False)
    terrain = db.Column(db.String(300), nullable=False)
    surface_water = db.Column(db.String(300), nullable=False)
    created = db.Column(db.String(300), nullable=False)
    edited = db.Column(db.String(300), nullable=False)
    url = db.Column(db.String(300), unique=True, nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.planet_id
    
    #The information is serialized
    def serialize_planet(self):
        return {
            "planet_id": self.planet_id,
            "name" : self.name,
            "climate" : self.climate,
            "population" : self.population,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter" : self.diameter,
            "gravity" : self.gravity,
            "terrain" : self.terrain,
            "surface_water" : self.surface_water,
            "edited": self.edited,
            "created": self.created,
            "url" : self.url,
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    fav_id = db.Column(db.Integer, primary_key = True)
    favorite = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Favorites %r>' % self.fav_id

    def serialize_favorite(self):
        return {
            "fav_id" : self.fav_id,
            "favorite" : self.favorite,
            "user_id" : self.user_id
        }

    def verification(self , fav_request, all_planet, all_people):
        planets = list(filter(lambda x : x["name"]==fav_request, all_planet))
        peoples = list(filter(lambda x : x["name"]==fav_request, all_people))
        return fav_request if  len(planets) > 0 or len(peoples) > 0 else None
