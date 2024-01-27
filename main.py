from AppOpener import open
from AppOpener import close
import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell


# set engine to pyttsx3 for text to speech in Python 
# and sapi5 in Microsoft speech 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 
# voice[1] - female
# voice[0] - male

def speak(audio):
        engine.say(audio)
        engine.runAndWait()


def takeCommand():
        
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
                r.listen_in_background
                print("Listening...")
        #       r.pause_threshold = 1
                audio = r.listen(source)

        try:
                print("Recognizing...")
                query = r.recognize_google(audio, language ='en-in')
                print(f"User said: {query}\n")

        except Exception as e:
                print(e)
                print("Unable to Recognize your voice.")
                return "None"
        
        return query



def hello(query):
            
        query=query.lower()

        if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

    
        elif 'play music' in query or "play song" in query:
                speak("Here you go with music")
                # music_dir = "G:\\Song"
                music_dir = "C:\\Users\Akhila\Music"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))


        elif 'time' in query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak('Current time is ' + time)


        elif 'exit' in query:
                speak("Thanks for giving me your time")
                exit()

                            

        elif 'close' in query:
                query = query.replace("close", "")
                if "app" in query:
                        query=query.replace("app","")
                speak('closing app'+query)              
                close(query)



        elif 'search' in query or 'play' in query:       
                query = query.replace("search", "")
                query = query.replace("play", "")               
                webbrowser.open(query)

            
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system('shutdown -s')

                                    
        elif "restart system" in query:
                speak("rebooting system")
                os.system("shutdown -t 5 -r -f")

                            
        elif "hibernate system" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call("shutdown /h")



        elif "log off system" in query or "sign out" in query:
                speak("Make sure all the application are closed before sign-out")
                subprocess.call("shutdown -l")

    
        elif "how are you" in query:
                speak("I'm fine, glad you me that")



        elif 'open' in query:
                query = query.replace("open", "")
                if ".com" in query:
                        speak("opening"+query)
                        webbrowser.open(query)

                elif "app" in query:
                        speak("opening"+ query)
                        query = query.replace("app", "")
                        open(query,match_closest=True)

                else:
                        subprocess.Popen(f'explorer /root,"search-ms:query={query}')
                        speak("searching for"+ query)



if __name__ == '__main__':
        speak("Welcome to jean screen reader")
        while True:
                speak("Ha ha ha ha")
                query = takeCommand().lower()
                if 'hello' in query:
                    speak("Ha ha ha ha")
                    query=query.replace("hello","")
                    hello(query)


                
