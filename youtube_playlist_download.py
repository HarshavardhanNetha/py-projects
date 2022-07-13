from pytube import Playlist
path = "/content/drive/MyDrive/CDVIDEO"

p = input("Enter th url of the playlist")
purl = Playlist(p)

print(f'Downloading: {p.title}')

for video in purl.videos:
    print(video.title)
    st = video.streams.get_highest_resolution()
    st.download(path)
    #video.streams.first().download()
