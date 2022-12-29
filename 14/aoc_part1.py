#!/usr/bin/env python3

import numpy as np

class Cave:
    def __init__(self, cave_data) -> None:
        self.x_min, self.x_max, self.y_max = self.find_size(cave_data)
        self.cave = np.full((self.y_max, (self.x_max - self.x_min)), ".", dtype=str)
        self.full = False
        self.sand_start = (0, 500 - self.x_min)
        self.sand = 0

        self.cave[self.sand_start] = "+"

        for line in cave_data:
            for x in range(len(line) - 1):
                start = (line[x][0] - self.x_min, line[x][1])
                end = (line[x + 1][0] - self.x_min, line[x + 1][1])
                self.draw_rock(start, end)
    
    def draw_rock(self, start, end):
        if start[0] != end[0]:
            step = 1
            if start[0] > end[0]:
                step = -1
            for x in range(start[0], end[0] + step, step):
                self.cave[end[1], x] = '#'
        else:
            step = 1
            if start[1] > end[1]:
                step = -1
            for y in range(start[1], end[1] + step, step):
                self.cave[y, end[0]] = '#'

    def find_size(self, cave_data):
        xs = list()
        ys = list()
        for line in cave_data:
            for point in line:
                xs.append(point[0])
                ys.append(point[1])
        return min(xs), max(xs) + 1, max(ys) + 1

    def drop_sand(self):
        if self.full:
            return
        
        self.sand += 1
        falling_sand_pos = [self.sand_start[0], self.sand_start[1]]
        sand_at_rest = False

        try:
            while not sand_at_rest:
                if self.cave[falling_sand_pos[0] + 1, falling_sand_pos[1]] not in ["#", "o"]: # check down
                    falling_sand_pos[0] += 1
                elif self.cave[falling_sand_pos[0] + 1, falling_sand_pos[1] - 1] not in ["#", "o"]: # check down left
                    falling_sand_pos[0] += 1
                    falling_sand_pos[1] -= 1
                elif self.cave[falling_sand_pos[0] + 1, falling_sand_pos[1] + 1] not in ["#", "o"]: # check down left
                    falling_sand_pos[0] += 1
                    falling_sand_pos[1] += 1
                else:
                    sand_at_rest = True
            
            self.cave[tuple(falling_sand_pos)] = "o"
        except:
            self.sand -= 1
            self.full = True


with open('input.txt') as f:
    cave_data = [[[int(z) for z in y.split(',')] for y in x.split(' -> ')] for x in f.read().split('\n')]

cave = Cave(cave_data)

while not cave.full:
    cave.drop_sand()

print(cave.sand)