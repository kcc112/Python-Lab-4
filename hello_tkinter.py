import tkinter as tk

init_pos_limit = 200.0
root = tk.Tk()
root.title('Task 4')
root.geometry('800x600')


class Field:
    def __init__(self):
        self.size = 1.5 * init_pos_limit + 1.5 * init_pos_limit
        self.half_size = self.size // 2
        self.sheeps = []
        self.canvas = tk.Canvas(root, height=self.size, width=self.size, bg="green")
        self.canvas.bind('<Button-1>', self.add_sheep)
        self.canvas.bind('<Button-3>', self.change_wolf_position)
        self.canvas.pack()
        self.wolf = self.canvas.create_rectangle(
            self.half_size - 2, self.half_size - 2, self.half_size + 2, self.half_size + 2, fill='red')

    def add_sheep(self, event):
        self.sheeps.append(self.canvas.create_rectangle(
            event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill="blue"))

    def change_wolf_position(self, event):
        self.canvas.coords(self.wolf, event.x - 2, event.y - 2, event.x + 2, event.y + 2)


field = Field()
root.mainloop()
