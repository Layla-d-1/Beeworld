# Student Name: Layla Dawood 
# Student ID:   23100624
# buzzness.py - module with class definitions for simulation of bee colony
#
# Version information:2 
# 2024-04-07 : Initial Version released
#


import random

class Bee:
    def __init__(self, ID, pos):
        self.ID = ID
        self.pos = pos
        self.age = 0
        self.carrying = False  # is the bee carrying nectar?
        self.inhive = True     # assume bees start in hive

    def step_change(self):
        # Random move
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dx, dy = random.choice(moves)

        new_x = self.pos[0] + dx
        new_y = self.pos[1] + dy

        # Clamp to 10x10 grid
        new_x = max(0, min(9, new_x))
        new_y = max(0, min(9, new_y))

        self.pos = (new_x, new_y)
        self.age += 1

        # Check for delivery to hive
        if self.carrying and self.pos == (5, 5):  # hive at (5,5)
            self.carrying = False
            return 'delivered'
        return None

    def get_pos(self):
        return self.pos


class Flower:
    def __init__(self, pos, nectar=5):
        self.pos = pos
        self.nectar = nectar

    def has_nectar(self):
        return self.nectar > 0

    def collect_nectar(self):
        if self.nectar > 0:
            self.nectar -= 1
            return True
        return False

    def get_pos(self):
        return self.pos

class Frame:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]  # 0–5 fill level

    def add_honey(self):
        for row in self.cells:
            for i in range(len(row)):
                if row[i] < 5:  # max fill level is 5
                    row[i] += 1
                    return True
        return False  # all cells full

    def get_cells(self):
        return self.cells

