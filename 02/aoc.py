#!/usr/bin/env python3

values = {
    'A':1,
    'X':1,
    'B':2,
    'Y':2,
    'C':3,
    'Z':3,
}

def get_score(round):
    opponent = values[round[0]]
    you = values[round[1]]

    if opponent == you:
        return 3 + you

    if you == 3: # scissors
        if opponent == 1: # rock
            return you
    
    if you == 2: # paper
        if opponent == 3: # scissors
            return you
    
    if you == 1:
        if opponent == 2: # scissors
            return you
    
    return 6 + you

def get_score2(round):
    choices = ['A', 'B', 'C']

    if round[1] == 'X':
        choice = choices[values[round[0]] - 2]
        return get_score([round[0], choice])

    if round[1] == 'Y':
        return get_score([round[0], round[0]])

    if round[1] == 'Z':
        try:
            choice = choices[values[round[0]]]
            return get_score([round[0], choice])
        except:
            return get_score([round[0], choices[0]])
    

def part1():
    with open('input.txt') as f:
        scores = sum([get_score(y) for y in [x.split(' ') for x in f.read().split('\n')]])
    
    return scores

def part2():
    with open('input.txt') as f:
        scores = sum([get_score2(y) for y in [x.split(' ') for x in f.read().split('\n')]])

    return scores

if __name__ == '__main__':
    print(part1())
    print(part2())