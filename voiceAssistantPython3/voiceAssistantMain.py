import speech_recognition as sr
import webbrowser
import re
import os
import pyttsx


def talkToMe(audio):
    print(audio)
    Vengine = pyttsx.init()
    engine.say('Good morning.')
    engine.runAndWait()



def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say somthing!")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said" + command + "\n")

    except sr.UnknownValueError:
        action(myCommand())
        print('Your last command couldn\'t be heard')
        command = myCommand()
    return command


def action(command):
    while('Assistant' in command):

        if 'open reddit' in command:
            reg_ex = re.search('open reddit (.*)', command)
        url = 'https://wwww.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        chrome_path = '/usr/bin/google-chrome'
        webbrowser.get(chrome_path).open(url)



while(True):
    action(myCommand())