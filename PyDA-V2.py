# By Samora Machel
__version__ = 1.2
__status__ = "Prototype"
__date__ = "29-04-2020"


import wolframalpha
import wikipedia
from gtts import gTTS
from playsound import playsound
import os
import Instagram_Bot_Interface as bot
import convert_video_to_audio as convert
import PythonPad as notebook
import webbrowser as web
import YouTubeDownloader as yt




from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from PyDA_ui import Ui_PyDA
from Text_ui import Ui_Dialog

class PyDa(QDialog, Ui_PyDA):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        global replyM

        self.Query.setPlaceholderText("Type \"> Help\" to get Information")

        self.Query.returnPressed.connect(self.onEnter)
        self.Query.textChanged.connect(self.checkCommand)

    def wkpd(self, request):
        # Request data from the wikipedia if and only if the data cannot be found in wolframalpha
        # After the data is extraced it is the stored into a variable called self.reply
        try:
            self.reply = wikipedia.summary(request)
            self.topLevel(self.reply)
            with open("PyDA-V2.log", "a") as file_:
                file_.write("\n\n\n"+request+" :\n\t\t"+self.reply)
        except Exception as e:
            self.topLevel(str(e))
            with open("PyDA-V2.log", "a") as file_:
                file_.write("\n\n\n"+request+" :\n\t\t"+str(e))


    def wlfa(self, request):
        # Requests data from the wolframalpha website,
        # the data returned is then stored in a variable know as self.reply
        # otherwise if the data is not availlable then data is requested from wikipedia
        client = wolframalpha.Client("TLPEHA-Q32TAV9U8H")
        try:
            res = client.query(request)
            self.reply = next(res.results).text
            self.topLevel(self.reply)
            with open("PyDA-V2.log", "a") as file_:
                file_.write("\n\n\n"+request+" :\n\t\t"+self.reply)

        except :
            self.wkpd(request)

    def topLevel(self,yourReply):
        # This is a function that creates a display widget which
        # displays data stored in the self.reply varible
        d = QDialog()
        textArea = Ui_Dialog(d)
        d.setObjectName("PyDa - Information Sector")
        textArea.Text.setText(yourReply)
        d.show()
        d.exec_()



    def speak(self):
        path = os.path.join(os.getcwd(), "temp.mp3")
        # speaks out the variable stored in the self.reply variable
        # it uses the google text to speech API
        # speech.speak(self.reply, "en")                    # uncomment if your using text-to-speech module
        try:
            temp = gTTS(self.reply)                             # If the top part is uncommented the comment then
            temp.save(path)                               # the whole try and except block
        except:
            os.remove(path)
            self.speak()
        # else:
        #     print("Not able to play sound")
        playsound(path)

    def checkCommand(self):
        replyM = self.Query.text()
        command = False
        data = replyM.split(" ")
        if data[0] == ">":
            self.setStyleSheet(
"#Query{\n"
"border: 2px solid #70FF75;\n"
"background-color: #E2F2E2;\n"
"border-radius: 10px;\n"
"color: black;\n"
"}\n"
           )
        else:
            self.setStyleSheet(
"#Query{\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"font-size: 13px;\n"
"}\n"
"#Query::focus\n"
"{\n"
"border: 2px solid rgb(115,194,251);\n"
"}\n"
            )




    def onEnter(self):
        # This is an event driven function which is executed once the Enter key is pressed
        # It execute the wlfa function
        replyM = self.Query.text()
        command = False
        data = replyM.split(" ")
        if data[0] == ">":
            command = True
        else:
            command = False

        if command:
            if "Instagram" in data:
                Bot = bot.Interface()
                Bot.main()
                Bot.app.mainloop()

            elif "Convert" in data:
                converter = convert.VideoConverter()
                converter.mainWindow()
                converter.VideoLocater()
                converter.root.mainloop()

            elif "Notebook" in data:
                Notebook = notebook.PythonPad()
                Notebook.Main_Window()
                Notebook.Menubar()
                Notebook.TextArea()
                Notebook.self_updates()
                Notebook.command_bindings()
                Notebook.KeyWords_Highlight()
                Notebook.root.mainloop()

            elif "Browser" in data:
                web.open("https://www.google.com/search?&q={}".format("+".join(data[2:])))

            elif "YouTube" in data:
                try:
                    Tube = yt.YouTube()
                    Tube.Download(location=os.getcwd(), url=str(data[2:]))
                except Exception as e:
                    print(e)
                    Tube = yt.YouTube()
                    Tube.Interface()
                    Tube.app.mainloop()
            elif "Help" in data:
                QMessageBox.information(self, "Information","""
This is PyDa your Personal Digital Assistant. It returns anwers to any
of your queries. Since it is an assistant, it does more than return
Query data. To tap more into its advanced use cases you use commands
There a basically 6 commands in total inclusive of the Help command

Type "> Help-More " for detailed information on use cases
                """)
            elif "Help-More" in data:
                help = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Informational Sector</title>
</head>
<body style="background-color: rgba(243, 239, 239, 0.856);">
<h4 id="Author-details">
    Creator - Samora Machel<br/>
    Version - 1.2 <br/>
    Status - Prototype <br/>
    Date - 29-04-2020 <br/>
</h4>
<hr/>

<h4 class="header" style="color:blue;"> WELCOME</h3>
    <br\>
    <pre style="color:black">This is PyDa your personal Digital Assistant
It gets all query that you input in the Entry box and even speak
out the answer after retrieving the query.
Basically it retrived any query you want. Think of it as
simplified webbrowser or wikipedia but it is not limited to querying
data only. It has capabilities to do much more when given specific
commands </pre>
<hr/>
<h4 class="header" style="color:blue;">COMMANDS</h3>
    <br\>
        <pre style="color:black">All commands start with a capital letter and are only executed
after you have initiated it with " > " symbol otherwise PyDa
will assume it is a normal query
There are basically 6 commands that PyDa Understands:</pre>
<hr/>
<ol>

    <li style="color:crimson">Help -
        <pre class="content", style="color:black">
            Gives a general overview of what PyDa does but for deeper
            and more detailed information on PyDa, the command "Help-More"
            is very useful
                ::: <span style="color:darkcyan;font-weight:bolder;">Executed as "> Help" or "> Help-More"</span></pre>
    </li>
    <hr style="width:50%;text-align:left;margin-left:0">
    <li style="color:crimson">Instagram -
        <pre class="content", style="color:black">
            PyDa has an inbuild Instagram Bot that automatically Follows
            and likes people from your instagram account. It can help
            you manage your instagram account incase your busy and sometimes
            don't have time for Instagram
            The Parameters it requires is :
                - The maximum ammount of people to follow
                - The maximum amount of like to give per person
                - To Prevent follow of people past what amount of followers

            To be on the safe side run the Instagram Bot once per day as
            Instagram algorithm might seize your account for one week
               :::<span style="color:darkcyan;font-weight:bolder;"> Executed as "> Instagram" </span></pre>
    </li>
    <hr style="width:50%;text-align:left;margin-left:0">
    <li style="color:crimson">Browser -
        <pre class="content", style="color:black">
            This command enables you to open your default browser, not only
            that but you can also query information like so
                ::: <span style="color:darkcyan;font-weight:bolder;">"> Browser who is SamoraMachel" </span>
            and you can opt to just open the browser like so
                ::: <span style="color:darkcyan;font-weight:bolder;">"> Browser" </span> </pre>
    </li>
    <hr style="width:50%;text-align:left;margin-left:0">
    <li style="color:crimson">YouTube -
        <pre class="content", style="color:black">
            PyDa has an inbult program to enable you to download programs from
            YouTube only. You can seperatly launch the program by typing
                :::<span style="color:darkcyan;font-weight:bolder;"> "> YouTube"</span>
            and then you enter the URL of the video to download and the
            location where the video will to downloaded to
            You can also opt to download the video without running the program
            PyDa allows you to do so.
            Like so,
                :::<span style="color:darkcyan;font-weight:bolder;"> "> YouTube URL-of-the-video"</span></pre>
    </li>
    <hr style="width:50%;text-align:left;margin-left:0">
    <li style="color:crimson">Notebook -
        <pre class="content", style="color:black">
            PyDa has an internal Notebook
            :::<span style="color:darkcyan;font-weight:bolder;"> Executed as "> Notebook"</span></pre>
    </li>
    <li style="color:crimson">Convert -
        <pre class="content", style="color:black">
            PyDa is also able to convert a video to audio. This can be made
            possible through the command
                :::<span style="color:darkcyan;font-weight:bolder;"> Executed as "> Convert" </span></pre>
    </li>
</ol>


</body>
</html>
                """
                self.topLevel(help)
            else:
                QMessageBox.warning(self, "Invalid Command", "Invalid Command !!!\nPlease input a valid command.")
        else:
            self.wlfa(replyM)
            with open("requests.log", "a") as file_:
                file_.write(replyM+"\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    samora = PyDa()
    samora.show()
    app.exec_()
