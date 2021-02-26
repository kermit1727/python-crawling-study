from urllib import parse

# 인덱스를 치환해준다.
baseUrl1 = "http://test.com/html/a.html"
print(">>>", parse.urljoin(baseUrl1, "b.html"))
print(">>>", parse.urljoin(baseUrl1, "sub/b.html"))
print(">>>", parse.urljoin(baseUrl1, "../index.html"))
print(">>>", parse.urljoin(baseUrl1, "../img/jpg"))
print(">>>", parse.urljoin(baseUrl1, "../css/img.css"))
