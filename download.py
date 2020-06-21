import pytube
link = "https://www.youtube.com/watch?v=mpjREfvZiDs"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()