from tkinter import *
window = Tk()
window.title("to-do list")
window.geometry("600x600")


def add(event):
    if entrybox.get() != "":
        Todo_list.insert(Todo_list.size(), entrybox.get())
        Todo_list.config(height= Todo_list.size())
        entrybox.delete(0, END)

def done():
    todo = []
    for t in Todo_list.curselection():
        todo.insert(t, Todo_list.get(t))
    label = Label(window, text= f"You finished: {[t for t in todo]}")
    label.pack()
    for i in reversed(Todo_list.curselection()):
        Todo_list.delete(i)
    Todo_list.config(height= Todo_list.size())

label = Label(window,
            text="To-Do list",
            font = ("Times New Roman", 10),
            width = 20
            )
label.pack()
# or Label(Text = "to-do list").pack
Todo_list= Listbox(window,
            bg= "black",
            selectmode= MULTIPLE,
            fg= "white",
            font = ("Times New Roman", 10),
            width = 20,
            activestyle = NONE
        )
Todo_list.pack()
Todo_list.config(height= Todo_list.size())



entrybox = Entry(window, font = ("Times New Roman", 10), width = 20)
entrybox.pack()
addButton = Button(window, text= "add things to be done", font = ("Times New Roman", 10), width = 20, command = add).pack()
doneButton = Button(window, text = "Done", command = done, font = ("Times New Roman", 10), width = 20).pack()
window.bind('<Return>', add)
window.mainloop()