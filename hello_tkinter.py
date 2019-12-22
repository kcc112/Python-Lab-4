import tkinter as tk


root = tk.Tk()

class Field:
    def __init__(self):
        self.canvas = tk.Canvas(root, height=400, width=400, bg="green")
        self.canvas.bind("<Button-1>", self.add_sheep)
        self.canvas.bind("<Button-3>", self.change_wolf_position)
        self.canvas.pack()
        self.wolf = self.canvas.create_rectangle(200 - 3, 200 - 3, 200 + 3, 200 + 3, fill="red")

    def add_sheep(self, event):
        self.canvas.create_rectangle(event.x - 3, event.y - 3, event.x + 3, event.y + 3, fill="blue")

    def change_wolf_position(self, event):
        self.canvas.coords(self.wolf, event.x - 3, event.y - 3, event.x + 3, event.y + 3)

field = Field()

root.mainloop()
