import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

site=requests.get(URL).text
soup=BeautifulSoup(site,"html.parser")
print(soup)
movies=soup.findAll(name="h3",class_="title")

moviestitles=[movie.getText() for movie in movies]
movies_titles=moviestitles[::-1]
with open(file="./movies.txt",mode="w",encoding="utf-8") as file:
    for movie in movies_titles :
        file.write(f"{movie}\n")
