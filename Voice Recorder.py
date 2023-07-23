from tkinter import *
from tkinter import messagebox
import sounddevice as sound               #pip install sounddevice
from scipy.io.wavfile import write        #pip install scipy
import wavio as wv                        #pip install wavio
import time                      

root=Tk()
root.title("Voice Recorder")
root.geometry("600x700+400+80")
root.resizable(False,False)
root.configure(bg="pink")

def Record():
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq,samplerate=freq,channels=2)
    sound.wait()
    write("recording.wav",freq,recording)

#timer
    try:
        temp=int(duration.get())
    except:
        print("Please Enter the right value")

    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1
        
        if(temp==0):
            messagebox.showinfo("Time Countdown","Time's up")
        Label(text=f"{str(temp)}",font="arial 40",width=4,bg="pink").place(x=240,y=590)

#icon
img_icon=PhotoImage(file="voicelogo.png")
root.iconphoto(False,img_icon)

#logo
photo=PhotoImage(file="Record.png")
my_image=Label(image=photo,bg="pink")
my_image.pack(padx=5,pady=5)


Label(root,text="Voice Recorder",font=("arial 30 bold"),bg="pink",fg="black").pack()

#entry
duration=StringVar()
entry=Entry(root,textvariable=duration,font="arial 30",width=15)
entry.pack(pady=10)
Label(text="Enter time in seconds",font="arial 15",bg="pink",fg="black").pack()

#Button
record=Button(root,text="Record",font="arial 20",fg="green",bd=0,command=Record).pack(pady=30)




root.mainloop()