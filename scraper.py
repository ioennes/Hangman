from tkinter.font import names
from bs4 import BeautifulSoup as bs
import requests
import re

url = r"https://www.imdb.com/chart/top-english-movies/"
response = requests.get(url)
soup = bs(response.text, "html.parser")

names = []

movies = soup.select('td.titleColumn')
for index in range(0, len(movies)):
    movie_string = movies[index].get_text().encode("ascii","ignore")
    movie_string = movie_string.decode()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    if index <= 99:
        movie = movie[3:-7].rstrip().lstrip()
    elif index > 99:
        movie = movie[4:-7].rstrip().lstrip() 

    names.append(movie)

names = "\n".join(names)

fname = open(f"movie_names.txt", "w")
fname.write(names)