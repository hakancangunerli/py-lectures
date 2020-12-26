import tkinter as tk #tkinter is built onto the standard library, no need to install anything it is available everywhere
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter") # this creates it
greeting.pack() # pack shows and fits the entire label into the gui
window.mainloop() # it's a req it'll keep the program running until it is closed. goes at the very end

