from tkinter import Tk, Label, Entry, Button
from tkinter.font import Font
from tkinter.messagebox import showinfo

root = Tk()
root.title("Keyboard Limit 0.1")

header_font = Font(family="Verdana", size=20)
property_font = Font(family="Verdana", size=16)

header = Label(root, text="Keyboard Limit 0.1", font=header_font)
header.grid(row=0, column=0)

limit_entry_label = Label(root, text="Limit:")
limit_entry_label.grid(row=1, column=0)
limit_entry = Entry(root)
limit_entry.grid(row=1, column=1)

command_entry_label = Label(root, text="Command:")
command_entry_label.grid(row=2, column=0)
command_entry = Entry(root)
command_entry.grid(row=2, column=1)


def save():
    showinfo("Save function", "You cannot save changes because the graphical interface is not ready yet.")


button = Button(root, text="Save", command=save)
button.grid(row=3, column=0)

root.mainloop()
