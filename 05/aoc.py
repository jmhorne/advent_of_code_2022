#!/usr/bin/env python3

def part1(crates, commands):

    for command in commands:
        for move in range(command[0]):
            crates[command[2] - 1].append(crates[command[1] - 1].pop())

    return get_message(crates)


def part2(crates, commands):

    for command in commands:
        crates[command[2] - 1] += crates[command[1] - 1][-command[0]:]
        crates[command[1] - 1] = crates[command[1] - 1][:-command[0]]

    return get_message(crates)


def get_message(crates):
    message = ""

    for stack in crates:
        message += stack.pop()
    
    return message


def build_crates(data):
    data = [list(x.replace('    ', '-').replace('[', '').replace(']', '').replace(' ', '')) for x in data]
    
    crates = [list() for x in range(len(data[0]))]

    [[crates[col].append(data[row][col]) for col in range(len(data[row])) if data[row][col] != '-'] for row in range(len(data) -1, -1, -1)]

    return crates


if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    
    commands = [[int(x) for x in y.split(' ') if x.isnumeric()] for y in data[1].split('\n')]

    crates = build_crates(data[0].split('\n')[:-1])
    print(part1(crates, commands))

    crates = build_crates(data[0].split('\n')[:-1])
    print(part2(crates, commands))