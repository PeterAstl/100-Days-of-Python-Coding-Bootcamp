
from bs4 import BeautifulSoup
import requests

# with open("./website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# anchortags = soup.find_all(name="a")
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)



response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

y = [int(score.text.split()[0]) for score in soup.find_all(class_ = "score")]
z = max(y)
x = y.index(z)
print(x)
print(z)

text = [score.text for score in soup.find_all(class_ = "titleline")]
print(text[x])

link = [score.find("a").get("href") for score in soup.find_all(class_ = "titleline")]
print(link[x])

score = [int(score.text.split()[0]) for score in soup.find_all(class_ = "score")]
print(score[x])