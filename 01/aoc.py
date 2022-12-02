#!/usr/bin/env python3

def part1():
    with open('input.txt') as f:
        return max([sum(z) for z in [[int(y) for y in x.split('\n')] for x in f.read().split('\n\n')]])

def part2():
    with open('input.txt') as f:
        sums = [sum(z) for z in [[int(y) for y in x.split('\n')] for x in f.read().split('\n\n')]]
        sums.sort(reverse=True)
        return sum(sums[:3])

if __name__ == '__main__':
    print("part 1: ", part1())
    print("part 2: ", part2())