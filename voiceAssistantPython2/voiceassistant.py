from gtts import gTTS
import speech_recognition as sr
import os
import re
import requests
import webbrowser
import smtplib
from weather import Weather
import wikipedia



def talkToMe(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)


   # tts = gTTS(text= audio, lang='en')
    #tts.save('audio.mp3')
    #os.system('mpg123 audio.mp3')


#listens for commands

talkToMe("I am ready for your command")

def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to contiune to listen for commands

    except sr.UnknownValueError:
        assistant(myCommand())
        print('Your last command couldn\'t be heard')
        command = myCommand()
    return command

#if statements for executing commands

def assistant(command):

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://wwww.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        chrome_path = '/usr/bin/google-chrome'
        webbrowser.get(chrome_path).open(url)

    elif 'open' in command:
        reg_ex = re.search('open (.*)', command)
        url = 'https://www.'
        domain = reg_ex.group(1)
        url = url + domain + '.com'
        chrome_path = '/usr/bin/google-chrome'
        webbrowser.get(chrome_path).open(url)

    if 'launch spotify' in command:
        spotify_path = '/snap/bin/spotify'
        os.startfile(spotify_path)

   # if 'ask wolfram' in command:
    #  reg_ex = re.search('ask wolfram (.*)', command)
    #    input = raw_input(reg_ex.group(1))
    #    res = client.query(input)
    #   answer = next(res.result).text
       # print(answer)
       # talkToMe(answer)




while True:
    assistant(myCommand())
