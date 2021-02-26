from urllib import request as req
from urllib.parse import urlencode

API = "https://api.ipify.org"

values = {
    'format': 'json'
}

print('before : ', values)
params = urlencode(values)    # 요청 형식에 맞게 url인코딩한다.
print('after : ', params)

# 사이트에서 요청하는 url : https://api.ipify.org?format=json'
url = API + "?" + params
print("요청 : ", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력 : ", reqData)
