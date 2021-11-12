import requests

res = requests.get("http://google.com")
print("응답코드: ", res.status_code) # 정상이면 200

# 스크래핑 오류 시 알려주는 코드
# res.raise_for_status()

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)