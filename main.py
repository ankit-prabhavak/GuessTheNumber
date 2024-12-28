#Project 2: Guess the number.

import random
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Lets start the game. Please guess the number and enter.")

n=random.randint(1,10)

a=-1
Guesses=0
while a!=n:
    a = int(input("Guess the number: "))
    Guesses+=1
    if(a>n):
        print("Too high")
        speak("Too high")
        
    elif(a<n):
        print("Too low")
        speak("Too low")
      
print(f"You have  guessed the number {n} in {Guesses} guesses.")
speak(f"You have  guessed the number {n} in {Guesses} guesses.")



