
from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

top_website = soup.find_all("h3", class_ = "title")

movie_titles = [movie.text for movie in top_website]
movies = movie_titles[::-1]

with open ("movies.txt", "w", encoding="utf-8") as myfile:
        for movie in movies:
            myfile.write(movie + "\n")