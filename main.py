import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_text = response.text

soup = BeautifulSoup(movies_web_text, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movies_array = []
for movie in movies:
    movie_text = movie.text
    movies_array.append(movie_text)

res = movies_array[::-1]

for mv in res:
    with open("movies.txt", "a") as movies_list:
        movies_list.write(mv + "\n")
