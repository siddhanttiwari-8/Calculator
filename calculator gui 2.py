from tkinter import *
import math

def click(event):
    text = event.widget.cget("text")
    try:
        if text == "=":
            result = eval(Scvalue.get())
            Scvalue.set(result)
        elif text == "C":
            Scvalue.set("")
        elif text == "sin":
            value = eval(Scvalue.get())
            result = math.sin(math.radians(value))
            Scvalue.set(round(result, 10))
        elif text == "cos":
            value = eval(Scvalue.get())
            result = math.cos(math.radians(value))
            Scvalue.set(round(result, 10))
        else:
            Scvalue.set(Scvalue.get() + text)
    except Exception:
        Scvalue.set("Error")

root = Tk()
root.geometry("400x600")
root.title("Calculator")

Scvalue = StringVar()
Scvalue.set("")
screen = Entry(root, textvar=Scvalue, font="Arial 20")
screen.pack(fill=BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["sin", "cos"],
    ["C"]
]

for row in buttons:
    frame = Frame(root)
    for btn in row:
        button = Button(frame, text=btn, font="Arial 18", relief=RAISED, border=5)
        button.pack(side=LEFT, expand=True, fill=BOTH, padx=5, pady=5)
        button.bind("<Button-1>", click)
    frame.pack(expand=True, fill=BOTH)  # fixed position

root.mainloop()
