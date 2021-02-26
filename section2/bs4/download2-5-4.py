from bs4 import BeautifulSoup

# CSS Selector를 활용해서 파싱하기
# 가장 많이 사용하는 기법이다.

html = '''
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
'''

soup = BeautifulSoup(html, "html.parser")

# CSS 아이디가 main인 div태그의 자식인 h1요소를 파싱한다.
h1 = soup.select("div#main > h1")
# 리스트 타입으로 반환된다.
print('h1 type >>>', type(h1))

# 결과값이 1개일지라도 리스트 타입으로 반환되므로
# 반복문을 사용해 연산해야한다.
for z in h1:
    print('z string >>>', z.string)

# 결과 값을 하나만 파싱하기 위해서는 _one을 사용한다.
h1_single = soup.select_one("div#main > h1")
print('str value >>>', h1_single.string)

# li태그를 전부 파싱하기
list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print('li >>>', li.string)

# id나 class명은 잘 변하지 않기 때문에 CSS Selector를 사용하는 편이
# 상당히 유용하다.
