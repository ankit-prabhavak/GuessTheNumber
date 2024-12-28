# Project 2: Guess the Number

## Description
This is a simple Python game where the user has to guess a randomly generated number between 1 and 10. The game gives feedback on whether the guess is too high, too low, or correct, and also tracks the number of guesses made. The game uses **text-to-speech** to speak out hints and the result.

## Features
- Random number generation between 1 and 10.
- User input to guess the number.
- Audio feedback using **pyttsx3** library.
- Keeps track of the number of guesses taken to find the correct number.
  
## Requirements
To run this project, you will need Python and the following dependencies:

- `pyttsx3` (Text-to-speech library)
- `random` (Python's built-in module)

You can install the required dependencies using the following command:

```bash
pip install pyttsx3
