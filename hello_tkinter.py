import tkinter as tk


root = tk.Tk()

def xy(event):
    canvas.create_rectangle(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="red")

canvas = tk.Canvas(root, height=400, width=400, bg="green")
canvas.pack()
canvas.bind("<Button-1>", xy)

root.mainloop()
