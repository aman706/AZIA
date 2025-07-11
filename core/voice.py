import pyttsx3
import speech_recognition as sr

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    print("Azia:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Internet connection issue.")
        return ""
