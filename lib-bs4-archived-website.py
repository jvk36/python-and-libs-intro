import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, 'html.parser')
# print(soup.text)
title_tags = soup.find_all("h3", class_="title")
sorted_titles = [title_tag.text+"\n" for title_tag in title_tags][::-1]
# print(sorted_titles)

with open("movies.txt", "w", encoding="utf-8") as file:
    file.writelines(sorted_titles)
