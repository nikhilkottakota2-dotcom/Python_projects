from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("flipcards_project/telugu_english_70_words.csv")
data_to_dict = data.to_dict(orient="records")

windows = Tk()
windows.title("Flash cards")
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

card =""
def next_card():
    global card
    card = random.choice(data_to_dict)
    canvas.itemconfig(card_title, text="Telugu",fill="black")
    canvas.itemconfig(card_word, text=card["Telugu"],fill="black")
    canvas.itemconfig(card_background,image=canvas_front_image)
    windows.after(3000,func=trans_card)
def trans_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=card["English"],fill="white")
    canvas.itemconfig(card_background,image=canvas_back_image)

canvas = Canvas(width=800,height=526)
canvas_front_image = PhotoImage(file=r"C:\python\100_days_bootcamp\flipcards_project\card_front.PNG")
canvas_back_image = PhotoImage(file=r"C:\python\100_days_bootcamp\flipcards_project\card_back.PNG")
card_background = canvas.create_image(400,263,image=canvas_front_image)
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))

cross_image=PhotoImage(file=r"C:\python\100_days_bootcamp\flipcards_project\wrong.PNG")
cross_button = Button(image=cross_image,command=next_card)
cross_button.grid(row=1,column=0)

right_image = PhotoImage(file=r"C:\python\100_days_bootcamp\flipcards_project\right.PNG")
right_button = Button(image=right_image,command=next_card)
right_button.grid(row=1,column=1)



next_card()

windows.mainloop()
