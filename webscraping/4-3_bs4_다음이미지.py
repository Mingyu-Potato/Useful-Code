# 이미지 다운받는 예제
import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=2021%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.find_all("a", attrs={"class":"toolTipTrigger"})
for i, image in enumerate(images):
    image_url = image.find("img")["src"]
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("movie_{}.jpg".format(i+1), "wb") as f:
        f.write(image_res.content)