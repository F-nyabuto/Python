from tkinter import *


window = Tk()
window.geometry('500x500')
def display():
    return Label(window, text=f'Check button is checked:{x.get()}').pack()

x = StringVar() #Yes/No
# x = IntVar() #0/1
# x = BooleanVar #True/False
check_button = Checkbutton(window,
                           text="I agree to the terms.",
                           variable=x,
                           onvalue="YES",
                           offvalue="No",
                           activeforeground="green",
                           activebackground="yellow",
                           command=display
                           )
check_button.pack()



# **Radio Buttons
color= ['red', 'black', 'green', 'blue']
def select():
    return Label(window, text=f'The color selected is {color[y.get()]}').pack()
y=IntVar()
for i in range(len(color)):
    Radiobutton(window,
                text=color[i],
                variable=y, # The radiobuttons with the same variable are gonna be grouped together
                value=i,
                command=select
    ).pack()
window.mainloop()