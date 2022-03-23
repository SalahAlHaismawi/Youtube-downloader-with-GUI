import tkinter as tk 
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

def createWidgets():
    #the text box where u paste your utube link.
    link_label = Label(root,text="Youtube URL: ", bg ="#E8D579")
    link_label.grid(row=1, column=0, pady=5, padx=5)
    
    root.link_text = Entry(root, width=60, textvariable=download_link)
    root.link_text.grid(row=1, column=1,pady=5, padx=5)
    
    #text box where your directory will be displayed
    destination_label = Label(root, text="Destination: ", bg="#E8D579")
    destination_label.grid(row=2, column =0, pady=5,padx=5)
    
    root.destination_text = Entry(root,width=45,textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=3,padx=3)
    #the browse button where you will be able to choose where to download the video
    browse_button = Button(root, text="Browse",command=browse,width=10,bg="#05E8E0")
    browse_button.grid(row=2, column=2, pady=1,padx=1)
    
    #the download button
    download_but = Button(root, text="Download Video" , command=download_video,width=25,bg="#05E8E0")
    download_but.grid(row=3,column=1,pady=3,padx=3)
    
    #this function allows the user to browse the files to choose a place to download.
def browse():
    
    download_dir=filedialog.askdirectory(initialdir="Your Directory Path")    
    
    download_path.set(download_dir)

    #this function allows the user to download the video
def download_video():
    
    url = download_link.get()
    folder = download_path.get()
    
    get_video = YouTube(url)
    get_stream=get_video.streams.first()
    get_stream.download(folder)
    
    messagebox.showinfo("Nice!!", "Download Successful! ")


root = tk.Tk()

root.geometry("600x120")
root.resizable(False,False)
root.title("Utube Downloader")
root.config(background="#000000")

download_link = StringVar()
download_path = StringVar()

createWidgets()

root.mainloop()