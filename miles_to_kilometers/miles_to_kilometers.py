from tkinter import *
miles = 0
km = 0
def calculate_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_label.config(text=f"{km}")


windows = Tk()
windows.title("Miles to Kilometer")
windows.minsize(width=100,height=50)

miles_input = Entry()
miles_input.grid(row=0,column=1)


miles_label = Label(text="Miles")
miles_label.grid(row=0,column=2)


is_equal_label= Label(text="Is Equal to:")
is_equal_label.grid(row=1,column=0)


result_label= Label(text="0")
result_label.grid(row=1,column=1)


label_km = Label(text="KM")
label_km.grid(row=1,column=2)


button_calculate = Button(text="Calculate",command=calculate_km)
button_calculate.grid(row=2,column=1)



windows.mainloop()