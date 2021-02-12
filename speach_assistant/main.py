import speech_recognition as srec
from time import ctime
import time
import playsound
import webbrowser
import os
import random #for generating files for the ausio file
from gtts import gTTS


r = srec.Recognizer()

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
    if "Hello" in voice_data:
        rai_speak("Hello There")
    if 'what is your name' in voice_data:
        rai_speak('My name RAI, and Mr Gift is my Creator')
    if "RAI what time is it" in voice_data:
        rai_speak(ctime())
    if "RAI search" in voice_data:
        search = recognize_speech("Hello, What do you want to search?")
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        rai_speak('Here is what I found for'+search)
    if "find location" in voice_data:
        location = recognize_speech("What is the location")
        url = 'https://google.nl/maps/place/'+location+'/&amp;'
        rai_speak('Here is the location')
        
    if "power off" in voice_data:
        rai_speak("Goodbye")
        exit()
    
time.sleep(1)
("Hello!.. How can I help you")

while 1:
    voice_data = recognize_speech()
    voice_response(voice_data)
    