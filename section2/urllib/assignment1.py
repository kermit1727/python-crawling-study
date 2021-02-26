from urllib import request as dw

imgUrl = "https://ssl.pstatic.net/tveta/libs/1307/1307612/"
imgUrl += "df56fbfd89493b919137_20201229131932149.jpg"

savePath = "download-file/ad1.jpg"

f1 = dw.urlopen(imgUrl).read()

with open(savePath, "wb") as saveFile1:
    saveFile1.write(f1)
    

print("Download Complete!")
