import pyjokes
import pyttsx3

joke = pyjokes.get_joke()
print('So the joke is :')
print(joke)

engine = pyttsx3.init()
engine.say(joke)
engine.runAndWait()