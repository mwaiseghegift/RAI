import speech_recognition as srec
from time import ctime
import time
import playsound
import webbrowser
import os
import random #for generating files for the ausio file
from gtts import gTTS


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
    if there_exists(['hello','RAI','anyone there']):
        rai_speak("Hello There")
    if there_exists(['what is your name','can I get your name']):
        rai_speak('My name rai, and Mr Gift is my Creator')
    if there_exists(["rai what time is it","Whats the time?"]):
        rai_speak(ctime())
    if there_exists(["rai search","search"]):
        search = recognize_speech("Hello, What do you want to search?")
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        rai_speak('Here is what I found for'+search)
    if there_exists(["find location","get location"]):
        location = recognize_speech("What is the location")
        url = 'https://google.nl/maps/place/'+location+'/&amp;'
        rai_speak('Here is the location')
        
    if there_exists(["power off","sleep"]):
        rai_speak("Goodbye")
        exit()
    
time.sleep(1)
("Hello!.. How can I help you")

while 1:
    voice_data = recognize_speech()
    voice_response(voice_data)
    