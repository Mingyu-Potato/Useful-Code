import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}

# 페이지에 따른 출력
for i in range(5):
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    
    print(str(i+1)+"페이지")

    # 정규식 찾기
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[0].find("div", attrs={"class":"name"}).get_text())

    # 조건에 따른 이름, 가격, 평점, 평점 수 출력
    for item in items:

        wow_badge = item.find("span", attrs={"class":"badge falcon"})
        if wow_badge:
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            rate = "평점 없음"
        rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            rate_cnt = "평점 수 없음"

        if rate != "평점 없음" and rate_cnt != "평점 수 없음":
            if float(rate) == 5.0 and int(rate_cnt) > 15:
                print(name, price, rate, rate_cnt)
            else:
                continue
