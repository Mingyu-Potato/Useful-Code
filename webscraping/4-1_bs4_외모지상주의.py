import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=641253&weekday=fri"
res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

# 제목 가져오기
cartoons = soup.find_all("td", attrs={"class":"title"})
# for cartoon in cartoons:
#     print(cartoon.a.get_text())
# print("https://comic.naver.com" + cartoons[0].a["href"])

# 평점 가져오기
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)