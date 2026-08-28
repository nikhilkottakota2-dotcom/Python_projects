from tkinter import *
import math
# ---------------- CONSTANTS ------------------------
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
#------------------TIMER RESET------------------------

running = True
def timer_reset():
    global running
    running = False
    canvas.itemconfig(timer_text,text="00:00")
    

#------------------TIMER MECHANISM--------------------
def start_timer():

    global running
    running = True
    minutes = int(user_ent.get())
    count_down(minutes * 60)
#------------------COUNTDOWN MECHANISM----------------
def count_down(count):

    global  running 
    if not running:
        return

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec<10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,count_down,count-1)

#------------------UI SETUP---------------------------

window = Tk()
window.title("pomodoro")
window.minsize(width=500,height=400)
canvas = Canvas(width=350,height=400,highlightthickness=0)

photo = PhotoImage(file=r"C:\python\100_days_bootcamp\pomodoro_timer\pomodoro_png.PNG")

canvas.create_image(175,200,image=photo)
timer_text=canvas.create_text(175,200,text="00:00",font=(FONT_NAME,45,"bold"))
canvas.grid(row=1,column=0,columnspan=3)

timer_label = Label(text="Timer",padx=60,pady=20,font=(FONT_NAME,42,"bold"))
timer_label.grid(row=0,column=1)

start_button = Button(text="Start",command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",command=timer_reset)
reset_button.grid(row=2,column=2)

check_marks = Label(text="✅",fg= "GREEN")
check_marks.grid(row=4,column=1)
#-------user input entry 

user_ent = Entry()
user_ent.grid(row=3,column=1)

window.mainloop()
