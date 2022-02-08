import speech_recognition as sr
# from gtts import gTTS for google TTS
import pyttsx3 # this is offline, so cool cool
import pygame
# import os
# import time
import playsound
#HAHA GOTEM

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()

pygame.mixer.init()

wWaAkKeE = "program"


while True:
    print("I'm listening...")
    text = get_audio()

    if text.count(wWaAkKeE) > 0:
        speak("Go ahead...")
        text = get_audio()

        if "hello" in text:
            speak("hello, how are you?")
            text = get_audio()
            if "good" in text:
                speak("I am good too!")

        if "what is your name" in text:
            speak("my name is ")

        if "vinay" in text:
            speak("Good Evening miss Thanvi, it's good to have you with us tonight. How are you?")
            text = get_audio()
            if "good" in text:
                speak("I am good too!")
        
        exit_bank = ["bye", "good night", "get lost", "get out", "exit", "quit"]
        for word in exit_bank:
            if word in text:
                speak("Have a nice day! Bye now.")
                exit()

        if "hardik" in text:
            speak("Hello keedai, now get lost")

        if "play mario" in text:
            mario = "C:/Users/Utkar/Dropbox/Atom programs/ProjectAI/06_-_Underground.mp3"
            playsound.playsound(mario)

        adventure_game = ["play an adventure game", "play a game", "fault in our stars game"]
        for word in adventure_game:
            if word in text:
                speak("Are you referring to the S I V G Protocol?")
                text = get_audio()
                if "yes" in text:
                    speak("Beginning S I V G protocol..... This will only take a few moments")
                    theme = pygame.mixer.music.load('C:/Users/Utkar/Dropbox/Atom programs/ProjectAI/PacificRimOST01.mp3')
                    pygame.mixer.music.set_volume(0.0)
                    pygame.mixer.music.play(-1)
                    speak("What is your name?")
                    name = get_audio()
                    player1 = str(name)
                    speak("nice to meet you"); speak(player1)
                    speak("Choose between the following characters: 'Hazel','Augustus','Isaac' ")
                    text = get_audio()
                    if "hazel" in text:
                        speak("You are Hazel. And this is your life partner Philip (your oxygen tank)!")
                    elif "augustus" in text:
                        speak("You are Augustus, also known as Gus. This is your inanimate but lively prosthetic leg!")
                    elif "isaac" in text:
                        speak("Welcome Sir Isaac. As you can see (pardon the irony please), this is a personalised game just for you! Here's your little glass eye. Kinda cool right?")
                    else:
                        speak("that was not there in the options")
                    
                elif "no" in text:
                    speak("ok then, escaping all S I V G procedures")
                else:
                    speak("that was not an answer to a yes or no type question")
