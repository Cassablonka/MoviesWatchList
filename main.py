# Import all the required packages
from bs4 import BeautifulSoup
import requests

# Get the URL of the desired output
response = requests.get('https://www.imdb.com/chart/top/')
contents = response.text

# Initialising for scrapping
soup = BeautifulSoup(contents, 'html.parser')

# Getting all the required elements

list_of_movies = soup.find_all(name='td', class_='titleColumn')
list_of_ratings = soup.find_all(name='td', class_='imdbRating')

movie_names = [movie.a.getText() for movie in list_of_movies]
movie_ratings = [rating.strong.getText() for rating in list_of_ratings]

movies = {movie_names[i]: movie_ratings[i] for i in range(100)}

count = 1
# Adding all the movies in a text file
with open('movie_list.txt', mode='a') as movie_list:
    for movie in movies:
        movie_list.write(f'{count}. {movie} - {movies[movie]} rating\n')
        count += 1
