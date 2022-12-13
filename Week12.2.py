from tkinter import *


def add():
    if entry.get() != "":
        todo.insert(todo.size(), entry.get())
        todo.config(height=todo.size())
        entry.delete(0, END)


def delete():
    for i in reversed(todo.curselection()):
        todo.delete(i)

    todo.config(height=todo.size())


window = Tk()
window.title("Todo")
window.geometry('600x600')
Label(text="TODO").pack()

todo = Listbox(window,
               bg="black",
               fg="White",
               font=("Arista Pro", 12),
               width=22,
               borderwidth=1,
               selectmode=MULTIPLE,  # Multiple options area selectable
               activestyle=NONE  # DOTBOX or UNDERLINE
               )
todo.pack()
todo.config(height=todo.size())

entry = Entry(window,font=("Arista Pro", 12), width=22)
entry.pack()
addButton = Button(window, text="Add",font=("Arista Pro", 12),width=20, command=add).pack()
deleteButton = Button(window, text="Done",font=("Arista Pro", 12),width=20, command=delete).pack()

window.mainloop()
