import speech_recognition as sr
import signal
from gpt_interface import gpt_resp_iter 
import os
import re
from gtts import gTTS
from playsound import playsound
from threading import Thread
import time

r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

print("audio calibration complete")

print('say "jarvis" to get started...')

# recognize speech using Wit.ai - it's not great but it works
WIT_AI_KEY = "BWO3WA5PIBOXGRH72SXCSFTWIGBQTD3Q"  # Wit.ai keys are 32-character uppercase alphanumeric strings

def text_to_speech(text):
    name =str(time.time_ns()) + ".mp3" 
    gTTS(text=text).save(name)
    playsound(name, True)
    os.remove(name)

# this is called from the background thread
def callback(recognizer, audio):
    try:
        new_text = recognizer.recognize_wit(audio, key=WIT_AI_KEY).lower()
        print("you: " + new_text)
    except sr.UnknownValueError:
        text_to_speech("I couldn't understand you")
        return
    except sr.RequestError as e:
        print("invalid resp; {0}".format(e))
        return
    except Exception as e:
        print("unknown error {0}".format(e))
        return
    
    if ("jarvis" in new_text):
        print("chat: " , end="", flush=True)

        phrase = ""
        phraseDelim = ".,!?"

        for tokens in gpt_resp_iter(new_text):
            print(tokens, end="", flush=True)
            phrase = phrase + tokens
            if (any(ch in phrase for ch in phraseDelim)):
                # Thread(target=text_to_speech, args = (f"{re.sub('[^ A-Za-z0-9]+', '', phrase)}",)).start()
                text_to_speech(f"{re.sub('[^ A-Za-z0-9]+', '', phrase)}")
                phrase = ""
        print("")

stop_listening = r.listen_in_background(m, callback)

def complete():
    stop_listening()
    os._exit()

signal.signal(signal.SIGINT, complete)

#signal.pause gets fucked by the say command - not sure why, but it exits after each say

while True:
    #spin
    a = 1