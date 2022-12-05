#!/usr/bin/env python3

def part1():
    with open('input.txt') as f:
        return sum([does_fully_contain(x) for x in [build_sections(y) for y in f.read().split('\n')]])

def part2():
     with open('input.txt') as f:
        return sum([does_overlap(x) for x in [build_sections(y) for y in f.read().split('\n')]])


def build_sections(in_str):
    return [build_section(x) for x in in_str.split(',')]

def build_section(in_str):
    r = [int(x) for x in in_str.split('-')]
    r[1] += 1

    return set([x for x in range(r[0], r[1])])

def does_fully_contain(sections):
    i = sections[0].intersection(sections[1])

    if i == sections[0] or i == sections[1]:
        return 1
    
    return 0

def does_overlap(sections):
    i = sections[0].intersection(sections[1])

    if len(i) > 0:
        return 1
    
    return 0

if __name__ == '__main__':
    print(part1())
    print(part2())