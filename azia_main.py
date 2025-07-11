from core.voice import speak, listen
from core.search import search_web
from core.wiki import ask_wikipedia
from core.tasks import run_task
from core.memory import remember, recall
from vision.detect import detect_face

speak("Hello, I am Azia, your assistant.")

while True:
    query = listen()

    if "exit" in query or "stop" in query:
        speak("Goodbye!")
        break

    elif "remember my name is" in query:
        name = query.split("is")[-1].strip()
        remember("name", name)
        speak(f"Got it! I'll remember your name is {name}.")

    elif "what's my name" in query:
        name = recall("name")
        speak(f"Your name is {name}" if name else "I don't know your name yet.")

    elif "wikipedia" in query:
        topic = query.replace("wikipedia", "").strip()
        speak("Searching Wikipedia...")
        answer = ask_wikipedia(topic)
        speak(answer)

    elif "detect face" in query:
        speak("Opening camera for face detection...")
        detect_face()

    elif any(x in query for x in ["open", "time", "youtube"]):
        result = run_task(query)
        speak(result)

    else:
        speak("Let me search that for you...")
        answer = search_web(query)
        speak(answer)

