import Tkinter
from appJar import gui
import os
import re
import requests
import webbrowser
import smtplib
from weather import Weather
import wikipedia

app = gui()

app.addLabel("title", "Personal Assistant")
app.setLabelBg("title", "Blue")



app.go()


window = tkinter.Tk()

