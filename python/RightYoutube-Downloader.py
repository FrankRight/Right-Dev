from pytube import YouTube

link = input("Paste the link to the video: ")

print("Downloading...")

YouTube(link).streams.first().download()

print("Video downloaded Successfully")