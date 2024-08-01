
from bs4 import BeautifulSoup       # html에서 데이터 추출 관련 함수 모듈 #beautifulsoup4

soup = BeautifulSoup(open("2_웹페이지크롤링.html", encoding="utf-8"), "html.parser")
print(soup)

fake_str = soup.find('p', id='box3').text
print( fake_str )


fake_str = soup.find('div', class_='fakecampus').find_all('p')
print(fake_str[2].get_text())

import urllib.request              # url 관련된 요청 함수 모듈

#예1) 웹사이트[페이지] HTML
url = "http://quotes.toscrape.com" #1.주소 입력
html = urllib.request.urlopen( url )            #2. 해당주소를 파이썬으로 가져오기

soup = BeautifulSoup( html.read() , "html.parser") #3. 해당 페이지의 데이터 가져오기

# 1.
# <span> : html의 특정 상자구역
print( soup.find_all("span") )
    # soup.find_all("태그명")  : 해당 태그명 검색
# 2.
# <div> : html의 특정 상자구역
print( soup.find_all( "div" , class_="quote")[0] )
    # soup.find_all("태그명") : 해당 태그명 검색 => 해당 태그의 클래스의 이름이 quote 검색

# 3.
for i in soup.find_all( "div" , class_="quote") :
    print( i )

for i in soup.find_all( "div" ,  class_="quote")  :
    print( i.find( 'span' , class_="text").get_text() )


