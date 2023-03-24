from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Sorry! Some error occured! Try again later.")
    print("Download is completed successfully!")


link = input("Enter the URL of the YouTube video: ")
Download(link)
