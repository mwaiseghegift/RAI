import speech_recognition as srec

r = srec.Recognizer()

def recognize_speech():
    with srec.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        
        try:
            voice_data = r.recognize_google(audio)
        except srec.UnknownValueError:
            print("Sorry! I didn't get you")
        except srec.RequestError:
            print("Sorry am currently down")
        return voice_data

def voice_response(voice_data):
    if 'what is your name' in voice_data:
        print('My name if retech voice assistant')
    
    
print("Hello!.. How can I help you")
voice_data = recognize_speech()
print(voice_data)

voice_response(voice_data)
    