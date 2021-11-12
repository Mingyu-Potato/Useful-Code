# beautifulsoup, lxml 패키지 설치
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# find
    # 형제, 부모, 자식 요소 하나 호출
    # rank1 = soup.find("li", attrs={"class":"rank01"})
    # print(rank1.a.get_text())
    # rank2 = rank1.next_sibling.next_sibling
    # rank3 = rank2.next_sibling.next_sibling
    # print(rank3.a.get_text())
    # rank2 = rank3.previous_sibling.previous_sibling
    # print(rank1.parent)

    # 형제 , 부모, 자식 요소 다 호출
    # rank2 = rank1.find_next_sibling("li")
    # print(rank2.a.get_text())
    # rank = rank1.find_next_siblings("li")

    # text 요소 호출
    # webtoon = soup.find("a", text="여신강림-175화")
    # print(webtoon)

# find_all
    # cartoons = soup.find_all("a", attrs={"class":"title"})
    # for cartoon in cartoons:
    #     print(cartoon.get_text())