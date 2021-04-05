import speech_recognition as srec
from time import ctime
import time
import playsound
import webbrowser
import os
import random #for generating files for the ausio file
from gtts import gTTS
import bs4
import requests
import urllib.request

r = srec.Recognizer()

def there_exists(words):
    for word in words:
        if word in voice_data:
            return True

def recognize_speech(ask=False):
    with srec.Microphone() as source:
        if ask:
            rai_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        
        try:
            voice_data = r.recognize_google(audio)
        except srec.UnknownValueError:
            rai_speak("Sorry! I didn't get you")
        except srec.RequestError:
            rai_speak("Sorry am currently down")
        return voice_data
    
def rai_speak(audio_string):
    text_to_speech = gTTS(audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) +'.mp3'
    text_to_speech.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def voice_response(voice_data):
    if there_exists(['hello','rai','anyone there']):
        rai_speak("Hello There")
    if there_exists(['what is your name','can I get your name']):
        rai_speak('My name rai, and Mr Gift is my Creator')
    if there_exists(["rai what time is it","Whats the time?"]):
        rai_speak(ctime())
    if there_exists(["I need help","rai I need help"]):
        rai_speak('call my lord, here is his phone number, 0712860997')
    if there_exists(["rai search","search","google"]):
        search = recognize_speech("Hello, What do you want to search?")
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        rai_speak('Here is what I found for'+search)
    if there_exists(["find location","get location"]):
        location = recognize_speech("What is the location")
        url = 'https://google.nl/maps/place/'+location+'/&amp;'
        rai_speak('Here is the location')
        
    if there_exists(['definition of','what is','who is']):
        definition = recognize_speech("What do you want to know")
        url = urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
        soup = bs4.BeautifulSoup(url,'lxml')
        definitions = []
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph))
            
        if definition:
            if definitions[0]:
                rai_speak('Sorry, please try again')
                
            elif definitions[1]:
                rai_speak(definitions[1])
            else:
                rai_speak(definitions[2])
        else:
            rai_speak("Sorry, I could not find that")
        
    if there_exists(["power off","sleep","shutdown"]):
        rai_speak("Goodbye")
        exit()
    
time.sleep(1)

while 1:
    voice_data = recognize_speech()
    voice_response(voice_data)
    