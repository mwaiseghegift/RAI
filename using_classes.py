import pyttsx3

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.rate = self.engine.getProperty('rate')
        
    def speaker_config(self):
        for voice in self.voices:
            self.engine.setProperty('voice', voice.id)
            print(voice.id)
        self.engine.setProperty('rate', 178)
        
    def say(self):
        self.engine.say("You are my lord")
        self.engine.runAndWait()
        
s1 = Speaker()
s1.speaker_config()
s1.say()