import tkinter

def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked") #overwriting the label
    my_label.config(text=input.get())

window=tkinter.Tk()
window.title("First GUI")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#Label:
my_label=tkinter.Label(text="1st Label") #This line as alone wont run, refer the next line 
my_label.config(text="New text")
my_label.grid(row=0,column=0) #We have to specify the component and then specify how it will be laid out on the screen 

#Button:
button1=tkinter.Button(text="Click me",command=button_clicked)
button1.grid(row=1,column=1) #to display button on the screen

button2=tkinter.Button(text="New button",command=button_clicked)
button2.grid(row=0,column=2) #to display button on the screen

#Entry:
input = tkinter.Entry(width=10)
print(input.get())
input.grid(row=2,column=3)


window.mainloop()
