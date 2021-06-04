import pytube
from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox as msg

class YouTube:
    def __init__(self):
        self.app = Tk()

        self.app.title("YouTube Downloader")
        self.app.resizable(False, False)

        self.url = StringVar()
        self.location = StringVar()
    
    def Interface(self):
        Label(self.app, text="URL: ").grid(row=0, column=0, sticky='w')
        Entry(self.app, textvariable=self.url, width=25).grid(row=1, column=0, sticky='w')

        Label(self.app, text="Destination:").grid(row=2, column=0, sticky='w')
        self.destination = Entry(self.app, textvariable=self.location, width=25)
        self.destination.grid(row=3, column=0, sticky='w')

        self.destination.bind("<Button-1>", self.Destination)
        Button(self.app, text="Get Resolution", command=self.StreamSelection).grid(row=4, column=0, sticky='e', pady=20)


    def Destination(self, Event=None):
        dest_folder = filedialog.askdirectory(title="Destination Folder")
        self.location = dest_folder
        self.destination.delete(0, END)
        self.destination.insert(0, os.path.basename(self.location))

    def StreamSelection(self):
        yt = pytube.YouTube(self.url.get())
        self.videos = yt.streams 
        self.top = Toplevel(self.app)
        self.top.title("Stream selection")
        counter = 1

        for v in self.videos:
            format = str(v).split(" ")
            videoType = format[2].split("mime_type=")[1]
            Label(self.top, text="{}.  Type: {} ".format(counter, videoType)).grid(row=counter, column=0, sticky='w')
            try:
                resolution = format[3].split("res=")[1]
                frames_per_second = format[4].split("fps")[1]
                Label(self.top, text="Resolution: {} ".format(resolution), fg='blue').grid(row=counter, column=1, sticky='w')
                Label(self.top, text="Frame Per Second: {} ".format(frames_per_second), fg='blue').grid(row=counter, column=2, sticky='w')
            except:
                abr = format[3].split('abr=')[1]
                codec = format[4].split('acodec=')[1]
                Label(self.top, text="Bit-rate: {} ".format(abr), fg='blue').grid(row=counter, column=1, sticky='w')
                Label(self.top, text="Codec: {} ".format(codec), fg='blue').grid(row=counter, column=2, sticky='w')
            counter += 1
        
        self.stream = IntVar(value=1)
        Entry(self.top, textvariable=self.stream).grid(row=counter+10, column=0, pady=20)
        Button(self.top, command=self.Download, text="Download").grid(row=counter+10, column=1, pady=20)
    
    def Download(self, location=None, url=None):
        if location==None and url==None:
            vid = self.videos[self.stream.get() - 1]
            self.top.destroy()
            msg.showinfo("Information", "This might take a while\nPlease bear with us")
            vid.download(self.location)
            msg.showinfo("Download Complete", "Succesfully Downloaded Video")
        else:
            self.app.withdraw()
            yt = pytube.YouTube(url)
            stream = yt.streams 
            msg.showinfo("Information", "This might take a while\nPlease bear with us")
            stream[3].download(location)
            msg.showinfo("Download Complete", "Succesfully Downloaded Video")
            self.app.destroy()




if __name__ == "__main__":
    sam = YouTube()
    sam.Interface()
    sam.app.mainloop()