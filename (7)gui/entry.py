import tkinter as tk

main = tk.Tk()

canvas1 = tk.Canvas(main, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(main)
canvas1.create_window(200, 140, window=entry1)


def getSquareRoot():
    x1 = entry1.get()

    label1 = tk.Label(main, text=float(x1) ** 0.5)
    canvas1.create_window(200, 230, window=label1)


button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

main.mainloop()