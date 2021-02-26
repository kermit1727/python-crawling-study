from urllib import request as req
from urllib.parse import urlencode

API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

values = {
    'ctxCd': '1012'
}

print('before : ', values)
params = urlencode(values)    # 요청 형식에 맞게 url인코딩한다.
print('after : ', params)

# 사이트에서 요청하는 url : https://api.ipify.org?format=json'
url = API + "?" + params
print("Request URL : ", url)

req_Data = req.urlopen(url).read().decode("utf-8")
# print(req_Data)

data_path = "download-file/보도자료.xml"
with open(data_path, "wb") as store:
    store.write(req_Data.encode())
