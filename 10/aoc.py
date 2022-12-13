#!/usr/bin/env python3

def part1(ins):
    reg = 1
    cycle = 1
    finds = {1:1}

    calculating = False

    while calculating or len(ins):
        if calculating:
            reg += curr[1]
            calculating = False
            cycle += 1
            finds[cycle] = reg
            curr = ins.pop(0)
        else:
            curr = ins.pop(0)

        calculating = curr[0] != "noop"
        
        cycle += 1
        finds[cycle] = reg

    marks = [20, 60, 100, 140, 180, 220]

    return sum([finds[m] * m for m in marks]), finds

def part2(ins):
    _, finds = part1(ins)
    sprite_pos = [0, 1, 2]
    screen_x = 0

    for c in range(1, 241):
        reg = finds[c]
        sprite_pos = [reg - 1, reg, reg + 1]

        if screen_x in sprite_pos:
            print("#", end='')
        else:
            print('.', end='')
        
        screen_x += 1
        if screen_x >= 40:
            screen_x = 0
            print()


with open('input.txt') as f:
    ins = [x.split(' ') for x in f.read().split('\n')]
    for i in range(len(ins)):
        if len(ins[i]) == 2:
            ins[i][1] = int(ins[i][1])

print(part1(ins.copy())[0])
part2(ins)