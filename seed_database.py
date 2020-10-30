"""Script to seed database."""

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

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    movies_in_db.append(crud.create_movie(movie['title'], 
                    movie['overview'],
                    datetime.strptime(movie['release_date'], "%Y-%m-%d"),
                    movie['poster_path']))

users_in_db = []
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'
    user = crud.create_user(email, password)
    users_in_db.append(user)

    for m in range(10):
        movie = choice(movies_in_db)
        score = randint(1, 5)
        crud.create_rating(score, movie, user)