from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User, Movie, UserMovie
from app.forms import LoginForm, RegistrationForm, MovieSearchForm
from app.best_movies_api import search_movie_by_title, get_movie_details
from functools import wraps


main = Blueprint('main', __name__)

@main.context_processor
def inject_forms():
    form = MovieSearchForm()  
    return dict(form=form)  

def login_required_redirect_index(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('main.login')) 
        return f(*args, **kwargs)
    return decorated_function

@main.route('/')
@login_required_redirect_index
def index():
    user_movies = UserMovie.query.filter_by(user_id=current_user.id).all()
    movies_in_user = []

    for user_movie in user_movies:
        movie_data = get_movie_details(user_movie.movie_id)
        if movie_data:
            movie_data['watched'] = user_movie.watched
            movie_data['favorite'] = user_movie.favorite
            movie_data['watchlist'] = user_movie.watchlist
            movies_in_user.append(movie_data)

    form = MovieSearchForm()
    return render_template('index.html', movies=movies_in_user, form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required_redirect_index
def logout():
    logout_user()
    db.session.close()
    return redirect(url_for('main.index'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
        
        if existing_user:
            flash('Username or Email already exists. Please choose a different one.')
        else:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('main.login'))

    for field, errors in form.errors.items():
        for error in errors:
            flash(f'Error in {getattr(form, field).label.text}: {error}')

    return render_template('register.html', form=form)
@main.route('/search', methods=['GET', 'POST'])
@login_required_redirect_index
def search():
    form = MovieSearchForm()
    page = request.args.get('page', 1, type=int)
    search_title = request.args.get('title', '')

    if form.validate_on_submit():
        title = form.title.data
        return redirect(url_for('main.search', title=title, page=1))

    movies = []
    total_pages = 0

    if search_title:
        movies, total_movies, total_pages = search_movie_by_title(search_title, page)

    return render_template('search_results.html', movies=movies, page=page, total_pages=total_pages, form=form, search_title=search_title)



@main.route('/movie/<int:id>', methods=['GET', 'POST'])
@login_required_redirect_index
def movie_detail(id):
    movie_data = get_movie_details(id)
    user_movie = UserMovie.query.filter_by(user_id=current_user.id, movie_id=id).first()

    return render_template('movie_detail.html', movie=movie_data, user_movie=user_movie)

@main.route('/movie/<int:id>/add', methods=['POST'])
@login_required_redirect_index
def add_movie(id):
    user_movie = UserMovie.query.filter_by(user_id=current_user.id, movie_id=id).first()
    if user_movie:
        user_movie.watched = request.form.get('watched') == 'on'
        user_movie.favorite = request.form.get('favorite') == 'on'
        user_movie.watchlist = request.form.get('watchlist') == 'on'
        if not (user_movie.watched or user_movie.favorite or user_movie.watchlist):
            db.session.delete(user_movie)
            flash("Movie removed from your collection as it's not watched, favorited, or on the watchlist.")
        else:
            flash("Updated movie status.")
    else:
        favorite = request.form.get('favorite')
        watched = request.form.get('watched')
        watchlist = request.form.get('watchlist')
        
        if favorite == 'on' or watched == 'on' or watchlist == 'on':
            user_movie = UserMovie(
                user_id=current_user.id,
                movie_id=id,
                watched=watched == 'on',
                favorite=favorite == 'on',
                watchlist=watchlist == 'on'  
            )
            db.session.add(user_movie)
            flash("Movie added to your collection.")
        else:
            flash("No status set. Movie was not added to your collection.")
    db.session.commit()

    return redirect(url_for('main.index'))
