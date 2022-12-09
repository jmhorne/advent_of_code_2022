#!/usr/bin/env python3

class Knot:
    def __init__(self, pos:list[int], head=None, tail=None):
        self.pos = pos
        self.head = head
        self.tail = tail
        self.visited = [self.pos.copy()]
    
    def add_tail(self, tail):
        if self.tail == None:
            tail.head = self
            self.tail = tail
        else:
            self.tail.add_tail(tail)
    
    def change_pos(self, change):
        self.pos[0] += change[0]
        self.pos[1] += change[1]

        if self.pos not in self.visited:
            self.visited.append(self.pos.copy())
        
        if self.tail:
            self.tail.calc_pos()
    
    def calc_pos(self):
        h_pos = self.head.pos
        t_pos = self.pos

        if abs(h_pos[0] - t_pos[0]) > 1 or abs(h_pos[1] - t_pos[1]) > 1:
            if h_pos[0] < t_pos[0]:
                t_pos[0] -= 1
            elif h_pos[0] > t_pos[0]:
                t_pos[0] += 1
            
            if h_pos[1] < t_pos[1]:
                t_pos[1] -= 1
            elif h_pos[1] > t_pos[1]:
                t_pos[1] += 1
        
        if t_pos not in self.visited:
            self.visited.append(t_pos.copy())
        
        if self.tail:
            self.tail.calc_pos()

def simulate(moves, num_knots):
    head = Knot([0, 0])

    for _ in range(num_knots - 2):
        head.add_tail(Knot([0, 0]))
    
    tail = Knot([0, 0])
    head.add_tail(tail)

    for move in moves:
        change = move_map[move[0]]
        for _ in range(move[1]):
            head.change_pos(change)
    
    return len(tail.visited)


move_map = {
    'U': [0, -1],
    'D': [0, 1],
    'L': [-1, 0],
    'R': [1, 0]
}

with open('input.txt') as f:
    moves = [(y[0], int(y[1])) for y in [x.split(' ') for x in f.read().split('\n')]]

print(simulate(moves, 2))
print(simulate(moves, 10))
