import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()

voices = engine.getProperty('voices')
if voices:
    engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Converts text to speech."""
    print('Fraddy: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    """Greets the user based on the time of day."""
    currentH = int(datetime.datetime.now().hour)
    if 0 <= currentH < 12:
        speak('Good Morning!')
    elif 12 <= currentH < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

def myCommand():
    """Listens for a command and returns it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please type your command.")
            return str(input('Command: ')).lower()

    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand. Please type the command.")
        return str(input('Command: ')).lower()
    except sr.RequestError as e:
        speak(f"Could not request results from Google service; {e}")
        speak("Please type your command instead.")
        return str(input('Command: ')).lower()
