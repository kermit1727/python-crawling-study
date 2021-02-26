from bs4 import BeautifulSoup

# Tag Selector를 활용해서 파싱하기

html = '''
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="http://www.google.com">google</a></li>
    <li><a href="http://www.tistory.com">tistory</a></li>
  </ul>
  </body></html>
'''

soup = BeautifulSoup(html, "html.parser")

# html문서에서 a태그를 모두 파싱한다.
links = soup.find_all("a")
print('links >>>', links)
print('links type >>>', type(links))

# find_all은 결과값을 리스트로 전달하므로 값이 하나뿐이라도
# 반복문을 이용해 연산해야한다.
for a in links:
    print('a >>>', a)
    print('a type>>>', type(a))

    txt = a.string
    href = a.attrs['href']
    print('txt >>>', txt, 'href >>> ', href)
    print("\n")

# 필터링
# string인자 값이 daum인 요소만 파싱한다.
a_filter = soup.find_all('a', string="daum")
print('a filter >>>', a_filter)

# 파싱해올 개수를 지정한다.
b = soup.find_all("a", limit=3)
print('b >>>', b)

# 문자열 요소만 파싱한다.
c = soup.find_all(string=["naver", "google"])
print('c >>>', c)
