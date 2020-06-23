import pytube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
link = "https://www.youtube.com/watch?v=vRt7JdyFBFc"
yt = pytube.YouTube(link)
stream = yt.streams.first()