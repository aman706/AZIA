import json
import os

MEMORY_FILE = "config/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f)

def remember(key, value):
    mem = load_memory()
    mem[key] = value
    save_memory(mem)

def recall(key):
    mem = load_memory()
    return mem.get(key, None)
