import pyttsx3

engine = pyttsx3.init()

bolbe = input('bol ki bolbo ? ')

engine.say(bolbe)
engine.runAndWait()