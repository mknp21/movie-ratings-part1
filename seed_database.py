"""Drop db, create db, and automatically populate db with data."""

import os
import json

from random import choice, randint
from datetime import datetime

import crud
import model
import server


os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()


# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    title, overview, poster_path = (
        movie["title"],
        movie["overview"],
        movie["poster_path"],
    )
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'


    # TODO: create a user here
user = crud.create_user(email, password)
# rating = create_rating(user, movie, score)

for i in range(10):
    # rand_rating = random.choice(rating)
    # rand_movie = random.choice(movies_in_db)

    random_movie = choice(movies_in_db)
    score = randint(1,5)

    crud.create_rating(user, random_movie, score)





    # TODO: create 10 ratings for the user
