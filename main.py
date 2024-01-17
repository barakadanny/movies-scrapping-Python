import requests
from bs4 import BeautifulSoup

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_web_text = response.text

soup = BeautifulSoup(movies_web_text, "html.parser")
movies = soup.find_all(name="h3", class_="title")
print(movies)


