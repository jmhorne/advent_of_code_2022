#!/usr/bin/env python3

import numpy as np

def check_visible(trees:list[list[int]], tree:list[int], change:list[int]):
    currTree = tree.copy()
    currTree[0] += change[0]
    currTree[1] += change[1]

    height = trees[tree[0]][tree[1]]

    isVisible = True

    while 0 <= currTree[0] < len(trees) and 0 <= currTree[1] < len(trees[0]):
        if trees[currTree[0]][currTree[1]] >= height:
            isVisible = False
            break
        currTree[0] += change[0]
        currTree[1] += change[1]

    return isVisible

def check_scenic(trees:list[list[int]], tree:list[int], change:list[int]):
    currTree = tree.copy()
    currTree[0] += change[0]
    currTree[1] += change[1]

    height = trees[tree[0]][tree[1]]

    view = 0

    while 0 <= currTree[0] < len(trees) and 0 <= currTree[1] < len(trees[0]):
        view += 1
        if trees[currTree[0]][currTree[1]] >= height:
            break
        currTree[0] += change[0]
        currTree[1] += change[1]

    return view

def check_north(trees:list[list[int]], tree:list[int]):
    return check_visible(trees, tree, [-1, 0])

def check_south(trees:list[list[int]], tree:list[int]):
    return check_visible(trees, tree, [1, 0])

def check_west(trees:list[list[int]], tree:list[int]):
    return check_visible(trees, tree, [0, -1])

def check_east(trees:list[list[int]], tree:list[int]):
    return check_visible(trees, tree, [0, 1])

def determine_scenic_score(trees:list[list[int]], tree:list[int]):
    score = check_scenic(trees, tree, [-1, 0])
    score *= check_scenic(trees, tree, [1, 0])
    score *= check_scenic(trees, tree, [0, -1])
    score *= check_scenic(trees, tree, [0, 1])

    return score

def part1(trees):
    visible_trees = (len(trees) * 2) + ((len(trees[0]) - 2) * 2)

    for row in range(1, len(trees) - 1):
        for col in range(1, len(trees[row]) - 1):
            if check_north(trees, [row, col]) or check_south(trees, [row, col]) or check_west(trees, [row, col]) or check_east(trees, [row, col]):
                visible_trees += 1

    return visible_trees

def part2(trees):
    highest = 0

    for row in range(1, len(trees) - 1):
        for col in range(1, len(trees[row]) - 1):
            score = determine_scenic_score(trees, [row, col])
            if score > highest:
                highest = score
    return highest


with open('input.txt') as f:
    trees = [[int(y) for y in list(x)] for x in f.read().split('\n')]

print(part1(trees))
print(part2(trees))
