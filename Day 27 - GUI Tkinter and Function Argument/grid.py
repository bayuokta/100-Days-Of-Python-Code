import tkinter

window = tkinter.Tk()
window.minsize(width=500, height=300)

# Component
my_label = tkinter.Label(text='Label')
my_button = tkinter.Button(text='Button')
my_new_button = tkinter.Button(text='New Button')
my_entry = tkinter.Entry()

# Layout
my_label.grid(row=0, column=0)
my_button.grid(row=1, column=1)
my_new_button.grid(row=0, column=2)
my_entry.grid(row=2, column=3)


window.mainloop()
