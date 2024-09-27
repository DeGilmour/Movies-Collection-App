from app import db, login_manager 
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    movies = db.relationship('UserMovie', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Movie(db.Model):
    id = db.Column(db.Integer, index=True, unique=True, primary_key=True)
    title = db.Column(db.String(128))
    director = db.Column(db.String(64))
    overview = db.Column(db.Text)
    release_date = db.Column(db.String(10))
    runtime = db.Column(db.Integer)
    poster_path = db.Column(db.String(128))

class UserMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    watched = db.Column(db.Boolean, default=False)
    favorite = db.Column(db.Boolean, default=False)
    watchlist = db.Column(db.Boolean, default=False)
    movie = db.relationship('Movie', backref='user_movies') 
