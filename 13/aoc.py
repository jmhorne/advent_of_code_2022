#!/usr/bin/env python3

def in_correct_order(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        if left > right:
            return False
        return None
    
    elif type(left) == list and type(right) == list:
        res = None
        pos = 0
        while res == None:
            try:
                res = in_correct_order(left[pos], right[pos])
            except:
                if len(left) < len(right):
                    res = True
                elif len(left) == len(right):
                    res = None
                else:
                    res = False
                break
            pos += 1
        
        return res
    
    if type(left) == int:
        left = [left]
    else:
        right = [right]
    
    return in_correct_order(left, right)


def part1():
    with open('input.txt') as f:
        packet_pairs = [[eval(y) for y in x.split('\n')] for x in f.read().split('\n\n')]

    correct = 0

    for pair in range(len(packet_pairs)):
        if in_correct_order(packet_pairs[pair][0], packet_pairs[pair][1]):
            correct += (pair + 1)
    
    print(correct)

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
    
    def add_node(self, new_val):
        if in_correct_order(self.val, new_val):
            if not self.right:
                self.right = Node(new_val)
            else:
                self.right.add_node(new_val)
        else:
            if not self.left:
                self.left = Node(new_val)
            else:
                self.left.add_node(new_val)
    
    def in_order(self):
        vals = []
        if self.left:
            vals += self.left.in_order()
        
        vals += [self.val]

        if self.right:
            vals += self.right.in_order()
        
        return vals

def part2():
    with open('input.txt') as f:
        packets = [eval(x) for x in f.read().split('\n') if x != '']
    dis1 = [[2]]
    dis2 = [[6]]
    
    head = Node(packets[0])

    for x in range(1, len(packets)):
        head.add_node(packets[x])
    
    head.add_node(dis1)
    head.add_node(dis2)
    
    vals = head.in_order()
    print((vals.index(dis1) + 1) * (vals.index(dis2) + 1))

part1()
part2()