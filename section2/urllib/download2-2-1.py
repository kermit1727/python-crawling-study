from urllib import request as dw

imgUrl = "https://i.pinimg.com/"
imgUrl += "474x/19/a2/96/19a296543e59c881c61f520d34bc5b3b.jpg"
htmlUrl = "http://google.com"

savePath1 = "download-file/kermit.jpg"
savePath2 = "download-file/index1.html"

dw.urlretrieve(imgUrl, savePath1)    # 매개변수로 경로와 저장 경로를 받는다.
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료!")

