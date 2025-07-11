import tkinter as tk
from tkinter import scrolledtext
import threading
from core.voice import speak, listen
from core.search import search_web
from core.wiki import ask_wikipedia
from core.tasks import run_task
from core.memory import remember, recall

def process_input(user_input, output_box):
    output_box.insert(tk.END, f"You: {user_input}\n")

    if "remember my name is" in user_input:
        name = user_input.split("is")[-1].strip()
        remember("name", name)
        response = f"Got it! I'll remember your name is {name}."
    
    elif "what's my name" in user_input:
        name = recall("name")
        response = f"Your name is {name}" if name else "I don't know your name yet."

    elif "wikipedia" in user_input:
        topic = user_input.replace("wikipedia", "").strip()
        response = ask_wikipedia(topic)

    elif any(x in user_input for x in ["open", "time", "youtube"]):
        response = run_task(user_input)

    else:
        response = search_web(user_input)
    
    output_box.insert(tk.END, f"Azia: {response}\n\n")
    speak(response)

def handle_send(entry, output_box):
    user_input = entry.get()
    entry.delete(0, tk.END)
    threading.Thread(target=process_input, args=(user_input, output_box)).start()

def handle_mic(output_box):
    query = listen()
    if query:
        output_box.insert(tk.END, f"You (mic): {query}\n")
        threading.Thread(target=process_input, args=(query, output_box)).start()

def run_gui():
    root = tk.Tk()
    root.title("Azia - Your AI Assistant")
    root.geometry("500x600")
    root.configure(bg="#1c1c1c")

    output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg="#2e2e2e", fg="white")
    output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(root, font=("Arial", 14), bg="#444", fg="white")
    entry.pack(padx=10, pady=(0,10), fill=tk.X, side=tk.LEFT, expand=True)

    send_btn = tk.Button(root, text="Send", command=lambda: handle_send(entry, output_box), bg="#4CAF50", fg="white")
    send_btn.pack(padx=5, pady=5, side=tk.LEFT)

    mic_btn = tk.Button(root, text="🎙️", command=lambda: handle_mic(output_box), bg="#f44336", fg="white")
    mic_btn.pack(padx=5, pady=5, side=tk.LEFT)

    root.mainloop()
