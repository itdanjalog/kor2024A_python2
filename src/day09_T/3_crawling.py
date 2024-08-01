from bs4 import BeautifulSoup
import urllib.request as ur  # URL 관련 요청 함수 모듈

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"

html = ur.urlopen(url )                 # 2 주소 열기
    # html : 하이퍼텍스트 마크업 언어 => 웹문서 [ 웹페이지 ]

soup = BeautifulSoup( html.read() , 'html.parser')

ul=soup.find( 'span' ,class_="spt_con dw").text
print( ul )



기사 = "https://v.daum.net/v/20240801164350442"
soup = BeautifulSoup( ur.urlopen(기사).read() , "html.parser" )
for i in soup.find_all("p") :
    print( i.text )

# 위에서 가져온 기사 본문를 파일에 저장
파일 = open("뉴스본문.txt" , "w", encoding='UTF-8' )
for i in soup.find_all("p") :
    파일.write( i.text+"\n")
파일.close()


