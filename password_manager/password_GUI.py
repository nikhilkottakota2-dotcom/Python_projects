from tkinter import *
import random

def generate_pass():
    words = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
    ]

    numbers = ['1','2','3','4','5','6','7','8','9']

    symbols = ['@','#','%','$','₹']
    g_password=""
    for w in range(1,6):
        g_password += random.choice(words)
    for n in range(1,4):
        g_password+=random.choice(numbers)
    for s in range(1,3):
        g_password += random.choice(symbols)
        password_shuffle = list(g_password)
        random.shuffle(password_shuffle)
        g_password = "".join(password_shuffle)
    # print(g_password)
    pass_entry.insert(0,g_password)


windows = Tk()
windows.title("Password")
windows.minsize(width=600,height=600)
canvas = Canvas(width=550,height=550)
photo = PhotoImage(file=r"C:\python\100_days_bootcamp\password_manager\password_png.PNG")
canvas.create_image(300,300,image=photo)
canvas.grid(row=1,column=1)

pass_label = Label(text="Password manager",font=("courier",40,"bold"))
pass_label.grid(row=2,column=1)

pass_ent = Label(text="Password",font=(24))
pass_ent.grid(row=4,column=0)

user_ent = Label(text="Username",font=(24))
user_ent.grid(row=3,column=0)

user_entry = Entry(font=("Arial",18))
user_entry.grid(row=3,column=1)

pass_entry = Entry(font=("Arial",18))
pass_entry.grid(row=4,column=1)

pass_generate = Button(text="Generate Password",font=("Arial",18),command=generate_pass)
pass_generate.grid(row=4,column=2)

login_button = Button(text="Login",font=("Arial",18))
login_button.grid(row=5,column=1)

sign_up = Button(text="Sign up",font=(20))
sign_up.grid(row=6,column=2)

windows.mainloop()