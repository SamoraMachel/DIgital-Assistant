# this is a program used to convert a video to audio 
# By Samora Machel
__version__ = 0.1
__status__ = "Prototype"
__date__ = "27-01-2020"
__maintainer__ = "samoraok@gmail.com"



from tkinter import *
from tkinter import messagebox, filedialog
import moviepy.editor as audicon
import os

class VideoConverter:

    # Creates the user interface for the VideoConverter
    def __init__(self):
        self.root = Tk()
        global VideoFile
        global AudioFile

        VideoFile = StringVar()
        AudioFile =StringVar()
    
    # This is the main interface where all 
    # the widgets enter
    def mainWindow(self):
        self.root.title("VideoConverter")
        self.root.resizable(False, False)

    # the function is used to ask the user 
    # for the video and the location to store the audio
    def VideoLocater(self):
        _frame = Frame(self.root).grid(row=0, column=0)

        # creates an interface to ask the user 
        # for the video
        Label(self.root, text="Search Video : ", justify=LEFT)     \
            .grid(row=0, column=0, padx=2, pady=2, sticky='w')
        self._videofile = Entry(self.root, textvariable=VideoFile, \
             justify=RIGHT, width=40)
        self._videofile.grid(row=0, column=1, padx=2, pady=2,   \
            sticky='e', columnspan=2)
        self._videofile.bind('<FocusIn>', self.open_videofile)

        # creates an interface to ask 
        # the user for the location and name of 
        # the audio to store
        Label(self.root, text="Select Download Location", justify=RIGHT)\
            .grid(row=1, column=0, padx=2, pady=2, sticky='w')
        self._audiofile = Entry(self.root, textvariable=AudioFile,      \
            justify=RIGHT, width=40)
        self._audiofile.grid(row=1, column=1, padx=2, pady=2,        \
            sticky='w', columnspan=2)
        self._audiofile.bind('<FocusIn>', self.open_audiofile)

        # initiates the conversion function
        Button(self.root, text='Convert', justify=CENTER, command              \
            =self.conversion ).grid(row=2, column=3, padx=2,        \
            pady=2, sticky='w')


    def open_videofile(self, Event=None):
        
        if self._videofile.get() == "":
            VideoFile = filedialog.askopenfilename(filetypes =      \
                [('Video Files', '*.mp4 *.ogv *.mpeg *.mov *.avi')] \
                , title="Select Video To Convert")
            self._videofile.insert('0', VideoFile)

        else:
            pass

    
    def open_audiofile(self, Event=None):
        if self._audiofile.get() == "":
            AudioFile = filedialog.asksaveasfilename(       \
                confirmoverwrite=True, initialfile =        \
                'Untitled.mp3', filetypes=                  \
                [('All Files', '*.*'),('mp3 files',         \
                '*.mp3'), ('Wave files', '*.wav'), ],       \
                title='Save Audio File')
            self._audiofile.insert('0', AudioFile)

        else:
            pass
    
    # converts the video to audio using 
    # the moviepy module
    def conversion(self):
        if self._videofile.get() == "" or   \
            self._audiofile.get() == "":    \
            messagebox.showinfo('Error',    \
            "Please select a Video and a suitable storage location",\
            "\nbefore pressing convert")
        else:
            _video = audicon.VideoFileClip  \
                (self._videofile.get())
            _video.audio.write_audiofile    \
                (self._audiofile.get())
            messagebox.showinfo('Success',  \
                os.path.basename(AudioFile.get())\
                +" Written\nSuccessfully")

if __name__ == '__main__':
    converter = VideoConverter()
    converter.mainWindow()
    converter.VideoLocater()
    converter.root.mainloop()