from urllib import request as dw

imgUrl = "https://encrypted-tbn0.gstatic.com/"
imgUrl += "images?q=tbn:ANd9GcQwrJBu9BS3___0r-NkOVI0MIQTsfOz4H6-vA&usqp=CAU"
htmlUrl = "http://google.com"

savePath1 = "download-file/elmo.jpg"
savePath2 = "download-file/index2.html"

f1 = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, 'wb')
saveFile1.write(f1)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!!!")

'''
urlretrieve => 얻어 온 자료를 바로 다운로드, 중간 작업을 할려면 저장후
                다시 읽어와야 함
urlopen => 정보를 가져와 변수에 저장 후 중간작업을 거쳐 다운
            받을때 용의함
'''
