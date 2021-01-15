import pyttsx3

engine = pyttsx3.init()
sound = engine.getProperty('voices')

print (sound)