#!/usr/bin/env python3

def find_priority(ruck):
    comp1 = set(ruck[:len(ruck) // 2])
    comp2 = set(ruck[len(ruck) // 2:])
    common = list(comp1.intersection(comp2))

    return letter_to_priority(common[0])

def letter_to_priority(l):
    if l.islower():
        return ord(l) - 96

    return ord(l) - 38

def find_group_priorities(rucks):
    r1 = set(rucks[0])
    r2 = set(rucks[1])
    r3 = set(rucks[2])
    id = list(r1.intersection(r2).intersection(r3))

    return letter_to_priority(id[0])

def part1():
    with open('input.txt') as f:
        return sum([find_priority(x) for x in f.read().split('\n')])

def part2():
    with open('input.txt') as f:
        rucks = f.read().split('\n')
        return sum([find_group_priorities(x) for x in [rucks[y:y + 3] for y in range (0, len(rucks), 3)]])

if __name__ == '__main__':
    print(part1())
    print(part2())