import pytube

# 다운 받을 동영상 URL지정
yt = pytube.YouTube("https://www.youtube.com/watch?v=LzmdGtzby2s")
videos = yt.streams.all()

# print('videos', videos)

'''for i in range(len(videos)):
    print(i, ', ', videos[i])
'''
down_dir = "download-file"

videos[0].download(down_dir)
