import os
import webbrowser
import datetime

def run_task(command):
    if "chrome" in command:
        os.system("start chrome")
        return "Opening Chrome browser."
    elif "notepad" in command:
        os.system("start notepad")
        return "Opening Notepad."
    elif "time" in command:
        return "Current time is " + datetime.datetime.now().strftime("%I:%M %p")
    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."
    else:
        return "I can't perform that task yet."
