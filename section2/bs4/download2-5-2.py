from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <h1>파이썬 BeautifulSoup study</h1>
    <p>Tag Selector</p>
    <p>CSS Selector</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print('soub >>>', soup, 'type >>>', type(soup))

# html서식을 예쁘게 정렬해준다.
print('prettify >>>', soup.prettify())

# 지정해준 html요소를 파싱한다.
h1 = soup.html.body.h1
print('h1 >>>', h1)
print('h1 string >>>', h1.string)
p1 = soup.html.body.p
print('p1 >>>', p1)

# 형제노드 사이를 이동할 수 있게해준다.
# 현재 p태그 사이에 줄바꿈이 있으므로 2번 사용해줘야한다.
p2 = p1.next_sibling.next_sibling
print('p2 >>>', p2)

# 현재 위치에서 이전에 위치한 요소를 파싱한다.
p3 = p1.previous_sibling.previous_sibling
print('p3 >>>', p3)

# 파싱해온 html태그에서 문자열 요소만 출력
print('h1 str value >>>', h1.string)
print('p1 str value >>>', p1.string)
print('p2 str value >>>', p2.string)

# 위 코드에 사용된 방식은 실제로는 크게 사용되지 않는다. html의 구조나 디자인이
# 변경되면 해당 코드는 제대로 작동하지 않기 때문이다.
# 그래서 주로 tag Selector보다 CSS Selector를 선호한다.




