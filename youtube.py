from pytube import YouTube

link="https://www.youtube.com/watch?v=AfR-lJghs4w"
youtube_1 = YouTube(link)

print(youtube_1.title)
print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all() #all format
videos = youtube_1.streams.filter(only_audio=True)
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm= int(input("enter : "))
videos[strm].download()
print('Successfully')



