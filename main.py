import speech_recognition as sr
import os
from tkinter import messagebox 
import tkinter
import tkinter as tk


recognizer_instance = sr.Recognizer() 

with sr.Microphone() as source:
    recognizer_instance.adjust_for_ambient_noise(source)
    print("speak")
    audio = recognizer_instance.listen(source)
    print("stop!")
try:
    text = recognizer_instance.recognize_google(audio, language="en-EN")
    root = tkinter.Tk()
    root.withdraw()
    x=messagebox.showinfo("error",text)
    root.destroy()

except Exception as e:
    print(e)
os.system("PAUSE")
