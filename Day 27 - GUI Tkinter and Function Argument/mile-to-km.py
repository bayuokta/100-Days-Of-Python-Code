import tkinter

window = tkinter.Tk()
window.title('Mile to KM Converter')

# variable
km = tkinter.DoubleVar()


# Function
def miles_to_km():
    km.set(float(entry_miles.get()) * 1.609344)


# Component
lbl_equals = tkinter.Label(text='is equal to')
lbl_miles = tkinter.Label(text='Miles')
lbl_km = tkinter.Label(text='KM')
entry_miles = tkinter.Entry()
entry_km = tkinter.Entry(textvariable=km, state='disabled')
btn_calculate = tkinter.Button(text='Calculate', command=miles_to_km)

# Layout
lbl_equals.grid(row=1, column=0)
entry_miles.grid(row=0, column=1)
lbl_miles.grid(row=0, column=2)
entry_km.grid(row=1, column=1)
lbl_km.grid(row=1, column=2)
btn_calculate.grid(row=2, column=1)

window.mainloop()
