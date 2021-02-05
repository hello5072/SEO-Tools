import pytube

url_list = ["www.youtube.com/watch?v=ghd6nH-LEMk",
"www.youtube.com/watch?v=QoE55FG8PVM",
"www.youtube.com/watch?v=u0Qq5jNIAR0",
"www.youtube.com/watch?v=TFQLRmNXfug",
"www.youtube.com/watch?v=5i9ndcs6hcA",
"www.youtube.com/watch?v=SmalLHJ4AvA",
"www.youtube.com/watch?v=xO6TKH6Rcgc",
"www.youtube.com/watch?v=2cgbeTsvp2c",
"www.youtube.com/watch?v=mK3-az5_hDA",
"www.youtube.com/watch?v=WSukvo4-Z1E",
"www.youtube.com/watch?v=v4m3MzOOqq0",
"www.youtube.com/watch?v=1VS2seKr6PM",
"www.youtube.com/watch?v=Ce9talOV9P4"]

def vid_download():
    for url in url_list:
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        # video = youtube.streams.get_highest_resolution_disregard_sound()
        '''
        leave this if lines for the future reference
        if youtube.streams.filter(res="1080p").first() is not None:
            video = youtube.streams.filter(res="1080").first()
        elif youtube.streams.filter(res="720p").first() is not None:
            video = youtube.streams.filter(res="720p").first()
        elif youtube.streams.filter(res="360p").first() is not None:
            video = youtube.streams.filter(res="360p").first()        
        '''
        video.download('C:/Users/brian.yang/Desktop/Adobe Download')
        print(video.title, video.resolution, youtube.description, url)

vid_download()
# .filter(progressive=True)