import tkinter as tk
from tkinter import messagebox


def do_sqrt():
    root = float(number_input.get())**0.5
    messagebox.showinfo("Square Root = ", root)


def do_square():
    square = float(number_input.get())**2
    messagebox.showinfo("Square = ", square)

main_window = tk.Tk()
main_window.title("Simple Calc")
number_input = tk.Entry(main_window)
button_sqrt = tk.Button(main_window, text="Square Root", command=do_sqrt)
button_sqrt.pack()
button_square = tk.Button(main_window, text="Square", command=do_square)
button_square.pack()
number_input.pack()

main_window.mainloop()