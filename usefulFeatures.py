import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, speed=0.04):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(speed)
    print()



