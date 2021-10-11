import pyttsx3
import datetime 
import speech_recognition as sr
import webbrowser as wb
import os
import pyautogui
import logging


redbot=pyttsx3.init()
voices = redbot.getProperty('voices')
redbot.setProperty('voice', voices[1].id) 

def speak(audio):
    print('R.E.D.B.O.T: ' + audio)
    redbot.say(audio)
    redbot.runAndWait()
   

def welcome():
    speak("How can I help you,boss") 

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=0.5 
        audio=c.listen(source)
    try:
        query = c.recognize_google(audio,language='en-US')
        query = query.strip()
        print("Red Bot: "+query)
        return query
    except sr.UnknownValueError:
        pass
    return "None"


if __name__  =="__main__":
    welcome()

    while True:
        query=command().lower()
        print(query)
        if "video" in query:
            meme =r"C:\Users\Admin\OneDrive - Hanoi University of Science and Technology\Documents\Power Point\704250_20204856_Đỗ Khánh Toàn Tuần 21.pptx"
            os.startfile(meme)
            pyautogui.sleep(3)
            pyautogui.moveTo(1079,622,0.25)
            pyautogui.click()
            pyautogui.sleep(2)
            pyautogui.press('F5')
        elif "continue" in query:
            pyautogui.press('right')
        elif "return" in query:
            pyautogui.press('left')
        # elif "table" in query:
        #     print("Tuan")
        # elif "hello" in query:
        #     print("Lo")
        