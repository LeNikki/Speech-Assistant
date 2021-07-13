import speech_recognition as sr     #imports the speech recognition library
import webbrowser                   #for opening web browser
import time                         #for time
import os                           #operating system
import playsound                    #package
import random                       #random module for number generat   ion
from gtts import gTTS               #google text to speech
from time import ctime              # will determine date and time

r = sr.Recognizer()                 #the Recognizer class is responsible for recognizing speech

def record_audio(ask = False):          #function record_audio, ask will be set to true if search is true
    with sr.Microphone() as source:     #you can use audio files but we want to use our microphone to talk
        if ask:
            nic_speak (ask)             #instead of just printing
        r.adjust_for_ambient_noise(source, duration=1)     #helps balance the noise
        audio = r.listen(source)        #variable audio is set to recognizer object (r), and there's a listen method to pass our source
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)  # variable for our source data; this will capture our voice data
        #Exceptions
        # Speech recognition using Google Speech Recognition
        #try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
        except sr.UnknownValueError:
            nic_speak("Google Speech Recognition could not understand audio")
        except sr.RequestError:
            nic_speak ("Sorry, my speech service is down")
        return voice_data

def nic_speak(audio_string):        #For input speech function
    tts = gTTS(text = audio_string, lang = 'en')   #tts (text to speech)
    r = random.randint (1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print (audio_string)
    os.remove(audio_file)

def respond(voice_data):    #function for respond
    if 'what is your name' in voice_data:   #note: the sentence should be lowercase
        nic_speak("My name is Nicole and I am your super gorgeous voice assistant.")
    if 'what time is it' in voice_data:
        nic_speak (ctime())
    if 'nicole are you dumb' in voice_data:
        nic_speak ("I am pretty. Actually, I am pretty dumb but we want to focus on the positive side.")
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?') #passing an optional parameter
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)  #will open the browser
        nic_speak("Here's what I found for "+search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?') #passing an optional parameter
        url = 'https://google.nl/maps/place/'+ location +'/&amp;'
        webbrowser.get().open(url)  #will open the browser
        nic_speak("Here's the location for "+ location)
    if 'play some music' in voice_data:
        url = 'https://www.youtube.com/watch?v=BC19kwABFwc&list=PLDIoUOhQQPlXqz5QZ3dx-lh_p6RcPeKjv'
        webbrowser.get().open(url)  #will open the browser
        nic_speak("Here's some latest pop music hits just for you")
    if 'nicole say' in voice_data:
        say = record_audio('What do you want me to say')  # passing an optional parameter
        nic_speak(say)
    if 'exit' in voice_data:  #will exit
        exit()


time.sleep(1)  #in seconds
nic_speak('Hi, how can I help you?')          #promt the user
print("Try:\n♣What is your name? \n♣Nicole, say...\n♣Nicole, are you dumb? \n♣What time is it?\n♣Search \n♣Find Location \n♣Exit \n♣Play some music")
while 1:   #while not exit
    print("\nAnalyzing...")
    voice_data = record_audio()
    print (voice_data)
    respond(voice_data)
