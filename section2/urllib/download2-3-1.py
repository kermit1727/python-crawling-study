from urllib import request as req
from urllib.parse import urlparse

url1 = "https://dreamhack.io/"
url2 = "http://www.naver.com?test='hi!'"

mem = req.urlopen(url1)

if mem.status == 200:
    print("Connect Success!!")

print("geturl : ", mem.geturl())
print("status : ", mem.status)
print("headers : ", mem.getheaders())
print("info : ", mem.info())
print("code : ", mem.getcode())

# 지정한 바이트 만큼의 파싱한 데이터를 가져온다. 이때 utf-8로 디코딩한다.
read_data1 = mem.read().decode("utf-8")

store_path = "download-file/file_read_data.html"

with open(store_path, 'wb') as st:
    st.write(read_data1.encode())    # Bytes Object

print(urlparse(url2))    # 각 부분을 파싱해준다. 많이 사용된다.





