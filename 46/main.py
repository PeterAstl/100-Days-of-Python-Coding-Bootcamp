from bs4 import BeautifulSoup
import requests


# url = "https://web.archive.org/web/20000815073341/http://billboard.com/charts/hot100.asp"
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#                   " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 OPR/124.0.0.0"
#           }
#
# response = requests.get("https://web.archive.org/web/20000815073341/http://billboard.com/charts/hot100.asp")
# soup = BeautifulSoup(response.text, "html.parser")
#
# top = soup.find_all("table")
#
# for table in top:
#     for tr in table.find_all("tr"):
#         for td in tr.find_all("b")[1:]:
#             print(td.text)
# #
# with open("new.txt", "r", encoding="utf-8") as file:
#     new_list = []
#     for line in file:
#          clean = line.strip().strip(",").strip('"')
#          new_list.append(clean)
#
#
# with open("new.txt", "w", encoding="utf-8") as f:
#     for item in new_list:
#         f.write(item + "\n")

