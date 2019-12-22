import tkinter as tk
from random import choice
from math import sqrt, inf

init_pos_limit = 200.0
sheep_move_dist = 5.0
wolf_move_dist = 50.0
root = tk.Tk()
root.title('Task 4')
root.geometry('600x600')


class Field:
    def __init__(self):
        self.size = 2 * (1.5 * init_pos_limit)
        self.half_size = self.size // 2
        self.sheeps = []
        self.canvas = tk.Canvas(root, height=self.size, width=self.size, bg='green')
        self.canvas.bind('<Button-1>', self.add_sheep)
        self.canvas.bind('<Button-3>', self.change_wolf_position)
        self.canvas.grid(row=1, column=0, columnspan=3)
        self.wolf = self.canvas.create_rectangle(self.half_size - 2, self.half_size - 2, self.half_size + 2, self.half_size + 2, fill='red')

    def add_sheep(self, event):
        self.sheeps.append(self.canvas.create_rectangle(event.x - 2, event.y - 2, event.x + 2, event.y + 2, fill='blue'))

    def change_wolf_position(self, event):
        self.canvas.coords(self.wolf, event.x - 2, event.y - 2, event.x + 2, event.y + 2)

    def sheep_move(self):
        for sheep in self.sheeps:
            direction = choice(['N', 'E', 'S', 'W'])
            cords = self.canvas.coords(sheep)

            if direction == 'E':
                self.canvas.coords(sheep, cords[0] + sheep_move_dist, cords[1], cords[2] + sheep_move_dist, cords[3])
            elif direction == 'W':
                self.canvas.coords(sheep, cords[0] - sheep_move_dist, cords[1], cords[2] - sheep_move_dist, cords[3])
            elif direction == 'N':
                self.canvas.coords(sheep, cords[0], cords[1] - sheep_move_dist, cords[2], cords[3] - sheep_move_dist)
            else:
                self.canvas.coords(sheep, cords[0], cords[1] + sheep_move_dist, cords[2], cords[3] + sheep_move_dist)

    def wolf_move(self):
        old_distance = inf
        sheep_nr = 0

        for sheep in self.sheeps:
            cords_sheep = self.canvas.coords(sheep)
            cords_wolf = self.canvas.coords(self.wolf)
            distance = sqrt((cords_sheep[0] - cords_wolf[0]) ** 2 + (cords_sheep[1] - cords_wolf[1]) ** 2)

            if distance < old_distance:
                old_distance = distance
                sheep_nr = self.sheeps.index(sheep)

        if old_distance < wolf_move_dist:
            sheep_removed = self.sheeps.pop(sheep_nr)
            self.canvas.delete(sheep_removed)
        else:
            cords_sheep = self.canvas.coords(self.sheeps[sheep_nr])
            cords_wolf = self.canvas.coords(self.wolf)

            wolf_x1 = cords_wolf[0] + (wolf_move_dist * (cords_sheep[0] - cords_wolf[0])) / old_distance
            wolf_y1 = cords_wolf[1] + (wolf_move_dist * (cords_sheep[1] - cords_wolf[1])) / old_distance
            wolf_x2 = cords_wolf[2] + (wolf_move_dist * (cords_sheep[2] - cords_wolf[2])) / old_distance
            wolf_y2 = cords_wolf[3] + (wolf_move_dist * (cords_sheep[3] - cords_wolf[3])) / old_distance

            self.canvas.coords(self.wolf, wolf_x1, wolf_y1, wolf_x2, wolf_y2)

    def step(self):
        if len(self.sheeps) is not 0:
            self.sheep_move()
            self.wolf_move()

field = Field()
button = tk.Button(root, text='Step', command=field.step).grid(row=0, column=0, sticky='W')
root.mainloop()
