import pyautogui, time, tkinter, threading
from tkinter import *
from tkinter.ttk import *

#commands
def ping_start():
    print("started")
    try:
        ping_user = username_entry.get()
        interval_per_ping = interval_entry.get()
        ping_started = True
        time.sleep(2)
        while True:
            if ping_start == False:
                break
            else:
                time.sleep(int(interval_per_ping) - 1)
                pyautogui.typewrite("@")
                time.sleep(0)
                pyautogui.typewrite(ping_user)
                pyautogui.press("enter")
                pyautogui.press("enter")
    except:
        #error window
        PingGUI_error = Tk()
        PingGUI_error.title("Error")
        PingGUI_error.configure(background="#7289DA")
        PingGUI_error.iconbitmap(r"Pictures\red_error.ico")
        PingGUI_error.geometry("230x100")
        PingGUI_error.resizable(0, 0)

        Label(PingGUI_error, text="An error has occured.", background="#7289DA", foreground="white", font="Sans 12 bold").place(x="33", y="15")

def ping_stop():
    ping_started = False

#main window
PingGUI = Tk()
PingGUI.title("PingSpammer")
PingGUI.configure(background="#7289DA")
PingGUI.iconbitmap("Pictures\ping.ico")
PingGUI.geometry("450x150")
PingGUI.resizable(0, 0)

#vars
ping_started = False
#Photo
discord_photo = PhotoImage(file="Pictures\cooldiscord.png")
Label(PingGUI, image=discord_photo, background="#7289DA").place(x="145")
#label 1:
Label(PingGUI, text="Username:", background="#7289DA", foreground="white", font="Sans 15 bold").place(x="10", y="50")
Label(PingGUI, text='Do not include an "@"', background="#7289DA", foreground="white", font="Sans 8").place(x="10", y="100")

#label 2:
Label(PingGUI, text="Interval:", background="#7289DA", foreground="white", font="Sans 15 bold").place(x="357", y="50")
Label(PingGUI, text="Second per ping.", background="#7289DA", foreground="white", font="Sans 8").place(x="357", y="100")

#text box 1
username_entry = Entry(PingGUI, width=17, background="white")
username_entry.place(x="10", y="80")

#text box 2
interval_entry = Entry(PingGUI, width=12, background="white")
interval_entry.place(x="357", y="80")

#buttons
start_button = Button(PingGUI, text="Start", command=ping_start).place(x="200", y="100")
stop_button = Button(PingGUI, text="Stop", command=ping_stop).place(x="200", y="125")

PingGUI.mainloop()