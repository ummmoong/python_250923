import urllib.request
from bs4 import BeautifulSoup
import re

#파일에 저장
f= open("clien.txt", "wt", encoding="utf-8")

#페이징처리
for i in range(0,10):
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" + str(i)
    print(url)
    #페이지 실행 결과 문자열
    data = urllib.request.urlopen(url)
    #스프 객체 새성
    soup = BeautifulSoup(data, 'html.parser')  
    #중고장터 매물 제목 
    list = soup.find_all("span", 
                         attrs={"data-role":"list-title-text"})
    for item in list:
        title = item.text.strip()
        print(title)
        f.write(title+"\n")

#페이지 실행 결과 문자열
data = urllib.request.urlopen(url)
#스프 객체 새성
soup = BeautifulSoup(data, 'html.parser')  
#중고장터 매물 제목 
list = soup.find_all("span", 
                     attrs={"data-role":"list-title-text"})
for item in list:
    title = item.text.strip()
    print(title)
    f.write(title+"\n")

f.close()



# <span class="subject_fixed" data-role="list-title-text" title="아이폰14 프로 1tb 무음 (가격인하)">
# 							아이폰14 프로 1tb 무음 (가격인하)
# </span>