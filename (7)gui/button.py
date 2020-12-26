import tkinter as tk #tkinter is built onto the standard library, no need to install anything it is available everywhere
window = tk.Tk()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

button.pack()
window.mainloop()