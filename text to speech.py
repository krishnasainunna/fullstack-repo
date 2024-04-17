from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
window=Tk()
window.title("Text To Speech")
window.geometry("900x450")
window.resizable(0,0)
window.iconbitmap("speak.ico")
'''we can set any image as a logo,to follow this code also
image_icon=PhotoImage(file="speak.png")
window.iconphoto(False,image_icon)'''
window['bg']="#305065"
'''to set the background color,to follow this code also
window.configure(bg="#305065")'''

engine=pyttsx3.init()

def speaknow():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')
    def setvoice():
        if gender=='Male':
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if text:
        if speed=="Fast":
            engine.setProperty('rate',250)
            setvoice()
        elif speed=='Normal':
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
            
def download():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')
    def setvoice():
        if gender=='Male':
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    if text:
        if speed=="Fast":
            engine.setProperty('rate',250)
            setvoice()
        elif speed=='Normal':
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
    
#Top Frame
top_frame=Frame(window,bg="white",width=900,height=100)
top_frame.place(x=0,y=0)

logo=PhotoImage(file="Speakerlogo.png")
L1=Label(top_frame,image=logo,bg="white")
L1.place(x=20,y=2)

L2=Label(top_frame,text="Text To Speech Application",bg="white",
         font="arial 20 bold",fg="red")
L2.place(x=150,y=30)

#==================================#
text_area=Text(window,font="Robote 20",bg="white",
               relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

L3=Label(window,text="VOICE",font="arial 15 bold",
         bg="#305065",fg="white")
L3.place(x=580,y=160)

L4=Label(window,text="SPEED",font="arial 15 bold",
         bg="#305065",fg="white")
L4.place(x=760,y=160)

gender_combobox=Combobox(window,values=['Male','Female'],
                         font="arial 15",width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set("Male")


speed_combobox=Combobox(window,values=['Fast','Normal','Slower'],
                         font="arial 15",width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set("Normal")

imageicon=PhotoImage(file="speak.png")
B1=Button(window,text="Speak",compound=LEFT,image=imageicon,
          width=130,font="arial 15 bold",bg="white",command=speaknow)
B1.place(x=550,y=280)

imageicon2=PhotoImage(file="download.png")
B2=Button(window,text="Save",compound=LEFT,image=imageicon2,
          width=130,font="arial 15 bold",bg="white",command=download)
B2.place(x=730,y=280)
window.mainloop()
