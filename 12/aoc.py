#!/usr/bin/env python3

from collections import defaultdict

class Node:
    def __init__(self, terrain, pos) -> None:
        self.pos = pos
        self.terrain = terrain
        self.val = terrain[pos[0]][pos[1]]
        self.real_val = self.val

        if self.real_val == ord('S'):
            self.real_val = ord('a')
        elif self.real_val == ord('E'):
            self.real_val = ord('z')

        self.neighbors = list()

    def add_neighbor(self, node):
        if node.real_val - 1 > self.real_val or self.val == ord('E'):
            return
        
        self.neighbors.append(node)
    
    def steps_to_end(self, seen=[]):
        if self.val == ord('E'):
            return 0

        paths = list()
        for n in self.neighbors:
            if n in seen:
                continue
            try:
                paths.append(1 + n.steps_to_end(seen + [self]))
            except:
                continue
        
        if not len(paths):
            raise Exception("no path")
        
        return min(paths)

with open('input.txt') as f:
    terrain = [[ord(y) for y in list(x)] for x in f.read().split('\n')]

graph = defaultdict(list)
start = ()
end = ()

for y in range(len(terrain)):
    for x in range(len(terrain[0])):
        graph[(y, x)] = Node(terrain, (y, x))
        if graph[(y, x)].val == ord('S'):
            start = (y, x)
        elif graph[(y, x)].val == ord('E'):
            end = (y, x)

neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
for n in graph:
    node = graph[n]

    for neighbor in neighbors:
        pos = (n[0] + neighbor[0], n[1] + neighbor[1])
        if pos in graph:
            node.add_neighbor(graph[pos])

print(graph[start].steps_to_end())