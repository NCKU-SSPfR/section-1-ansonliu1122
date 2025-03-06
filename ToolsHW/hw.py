import webbrowser
import sys
import time
import random
import os


VIDEO_SRC = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def input_math():
    while True:
        user_input = input("1 times 1 = ? ")
        if user_input == 1: 
            open_video()
        elif user_input == "exit":
            sys.exit()
        else:
            print("Wrong! Try again.")
            open_video()

def open_video():
    webbrowser.open(VIDEO_SRC)
    os.system("echo 'Rickroll incoming...'")

input_math()