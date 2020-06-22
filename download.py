import pytube
<<<<<<< HEAD
link = "https://www.youtube.com/watch?v=mpjREfvZiDs"
=======
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

link = "https://www.youtube.com/watch?v=vRt7JdyFBFc"
>>>>>>> 6b359dac4da4673bcb4312c268d0f685bb6a8fb1
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()