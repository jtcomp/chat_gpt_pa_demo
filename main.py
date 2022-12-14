import speech_recognition as sr
import signal
from gpt_interface import gpt_resp_iter 
import os
import re
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

print("audio calibration complete")

print('say "GPT" to get started...')

# recognize speech using Wit.ai - it's not great but it works
WIT_AI_KEY = "BWO3WA5PIBOXGRH72SXCSFTWIGBQTD3Q"  # Wit.ai keys are 32-character uppercase alphanumeric strings

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition

    try:
        new_text = recognizer.recognize_wit(audio, key=WIT_AI_KEY).lower()
        print("you: " + new_text)
    except sr.UnknownValueError:
        print("wit could not understand audio")
        return
    except sr.RequestError as e:
        print("invalid resp; {0}".format(e))
        return
    except Exception as e:
        print("unknown error {0}".format(e))
        return
    
    if ("jarvis" in new_text):
        print("chat: " , end="", flush=True)
        for tokens in gpt_resp_iter(new_text):
            print(tokens, end="", flush=True)
            os.system(f"""say '{re.sub('[^ A-Za-z0-9]+', '', tokens)}'""") ## lol OSX for the win 
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