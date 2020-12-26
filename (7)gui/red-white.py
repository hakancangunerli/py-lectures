import tkinter as tk #tkinter is built onto the standard library, no need to install anything it is available everywhere
window = tk.Tk()
#greeting.pack() # pack shows and fits the entire label into the gui
label = tk.Label(
    text="Hello, Tkinter",fg = "red", bg = "black") # also can add width
#https://www.tutorialspoint.com/python/tk_label.htm
label.pack()
window.mainloop()