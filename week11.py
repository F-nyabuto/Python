from tkinter import *  # (imports everything form tkinter)
# Creating a window
def delete():
    entry.delete(0, END) #remove characters from 0 to end

def click():
    username = entry.get()
    print(f'Hello {username}')
win = Tk()
win.title("Python Class")

win.geometry('1000x800')
icon = PhotoImage(file='hi.png')
win.iconphoto(True, icon)

win.config(background="#aaf0d3")
label = Label(win,
              text="Hi, this is a mushroom",
              font=('Arial', 20, "bold"),
              fg='Yellow',
              bg='Black',
              padx = 20,
              pady=30,
              relief='ridge',
              image=icon,
              compound='left'
              )
# label.pack()
label.place(x=0, y=0)

button = Button(win,
                text="Click",
                font=("Comic sans", 10),
                fg="Blue",
                bg="white",
                activebackground="gray",
                activeforeground="Blue",
                width=20,
                command=click
                )
# button.pack()
button.place(x=500, y=100)

entry = Entry(win,
              font=("Arial", 9),
              fg= "white",
              bg="grey",
              relief="ridge"
              )
entry.insert(0, 'Password')
entry.place(x=500, y=200)
Button(win, text="Delete", command=delete).pack()
win.mainloop()

