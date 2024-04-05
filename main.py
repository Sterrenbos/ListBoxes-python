from tkinter import *


def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


window = Tk()
listbox = Listbox(window, bg="light yellow", font=("Constancia", 35), width=12, selectmode=MULTIPLE)

listbox.pack()
listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "bread")
listbox.insert(4, "soup")
listbox.config(height=listbox.size())
entryBox = Entry(window)
entryBox.pack()
submit_button = Button(window, text="submit", command=submit, )
submit_button.pack()
add_button = Button(window, text="add", command=add, )
add_button.pack()
delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

window.mainloop()