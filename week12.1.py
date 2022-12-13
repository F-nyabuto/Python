from tkinter import *
from tkinter import colorchooser


def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())
    entrybox.delete(0, END)


def submit(event):
    foodList = []
    for food in listbox.curselection():
        foodList.insert(food, listbox.get(food))

    label = Label(window, text=f"You ordered: {[f for f in foodList]}")
    label.pack()


def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    listbox.config(height=listbox.size())


window = Tk()

# list box
listbox = Listbox(window,
                  bg="Yellow",
                  font=("Arista Pro", 25),
                  width=9,
                  selectmode=MULTIPLE,  # Multiple options area selectable
                  activestyle=NONE  # DOTBOX or UNDERLINE
                  )
listbox.pack()
listbox.insert(0, "Pizza")
listbox.insert(1, "Sandwich")

listbox.config(height=listbox.size())  # so it wont take the whole length

entrybox = Entry(window)
entrybox.pack()

addButton = Button(window, text="Add", command=add).pack()
submitButton = Button(window, text="Submit", command=submit).pack()
deletButton = Button(window, text="Delete", command=delete).pack


# ***SLIDESCALE

def submit_scale():
    return Label(window, text=f"Submitted scale value: {scale.get()}").pack()


scale = Scale(window,
              from_=100,
              to=0,
              length=300,
              orient="horizontal",
              font=("Candara", 10),
              showvalue=0,  # Hides current value of the scale
              tickinterval=10,  # adds numeric indicators
              resolution=5,  # Changing increment of the slider
              troughcolor="Yellow",
              fg="Lime",
              bg="Black"
              )

scale.set((scale['from'] - scale['to']) / 2 + scale["to"])
scale.pack()

scale_burron = Button(window, text="Submit scale value", command=submit_scale).pack()


# COLORCHOOSER
def choose():
    # first item is the rgb value and the second is the hex value
    color = colorchooser.askcolor()
    colorHex = color[1]
    # print(color)
    listbox.config(bg=colorHex)
    scale.config(troughcolor=colorHex)


Button(window, text="Choose color: ", command=choose).pack()

window.bind('<Return>', submit)  # to bind enter key to submit in tkinter window

window.mainloop()