from cProfile import label
from tkinter import *
import tkinter

def km_to_m():
    km=float(km_input.get())
    meter=km*1000
    meter_result.config(text=meter)

window=tkinter.Tk()
window.title("Kilometers to meters")
window.config(padx=20,pady=20)

km_input=Entry(width=7)
km_input.grid(row=0,column=1)

km_label=Label(text="km")
km_label.grid(row=0,column=2)

is_equal=Label(text="is equal to")
is_equal.grid(row=1,column=0)

meter_result=Label(text="0")
meter_result.grid(row=1,column=1)

meter_label=Label(text="m")
meter_label.grid(row=1,column=2)

calculate_button=Button(text="Calculate",command=km_to_m)
calculate_button.grid(row=2,column=1)

window.mainloop()