import tkinter
from tkinter import ttk


top = tkinter.Toplevel()
top.title("See")

e = ttk.Combobox(top, values=['en', 'de'])
e.pack()

print(e.winfo_class())
top.mainloop()
