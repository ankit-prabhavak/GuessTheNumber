#Project 2: Guess the number.

import random
import pyttsx3

engine = pyttsx3.init()
engine.say("Lets start the game. Please guess the number and enter.")
engine.runAndWait()

n=random.randint(1,10)

def speak(text):
    engine.say(text)
    engine.runAndWait()


a=-1
Guesses=0
while a!=n:
    a = int(input("Guess the number:"))
    Guesses+=1
    if(a>n):
        print("Too high")
        speak("Too high")
        
    elif(a<n):
        print("Too low")
        speak("Too low")
      
print(f"You have  guessed the number {n} in {Guesses} guesses.")
speak(f"You have  guessed the number {n} in {Guesses} guesses.")



