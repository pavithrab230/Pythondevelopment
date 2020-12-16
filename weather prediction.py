import requests
from bs4 import Beatifulsoup
search = "weather in Erode"
url = f"https://www.google.com/search?&q={search}"
r = requests.get(url)
s =Beatifulsoup(r.text,"html.parser")
update = s.find("div",class_="BNeawe").text
print(update)
