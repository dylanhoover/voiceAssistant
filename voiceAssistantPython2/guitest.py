import Tkinter
from appJar import gui
#import voiceassistant

app = gui()


sUsr = "Dylan"
sPswd = "hello"

def press(button):
    if button == "Close":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pswd = app.getEntry("Password")
  

   # if button == "Submit" and (usr == sUsr) and (pswd == sPswd):
   #     app.startSubWindow("Assistant")

app.startSubWindow("Login")
app.addLabel("title", "My voice assistant")
app.setLabelBg("title", "blue")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
app.addButton("Submit", "Close", press)
app.setFocus("Username")

app.go(startWindow="Login")
