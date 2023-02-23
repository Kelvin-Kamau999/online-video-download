from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    save_dir = filedialog.askdirectory()
    
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)