"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    """Show the homepage"""

    return render_template("homepage.html")

@app.route('/movies')
def show_movies():
    """Display movies in db"""

    movies = crud.get_movie()

    return render_template('all_movies.html', movies = movies)

@app.route("/movie/<movie_id>")
def show_movie_id(movie_id):
    """Show details of a movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template("movie_details.html", movie = movie)

# @app.route("/users")
# def show_users():
#     """Display user info"""

#     users = crud.get_users()

#     return render_template("users.html", users = users)


# @app.route("/movie/<user_id>")
# def show_user_id():
#     """Show details of a user"""

#     user = crud.get_user_by_id()

#     return render_template("user.html", user = user)



if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)



# Column name     Notes

# user_id      integer, autoincrementing primary key

# email         string, no char limit, unique

# password      string, no char limit