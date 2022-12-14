#!/usr/bin/env python3

from numpy import prod

class Monkey:
    def __init__(self, items, op, test, true_monkey, false_monkey, all_monkeys, relief=1) -> None:
        self.items = items
        self.op = op
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.items_inspected = 0
        self.all_monkeys = all_monkeys
        self.relief = relief
    
    def inspect(self, old):
        return eval(self.op)
    
    def get_item(self, item):
        self.items.append(item)
    
    def inspect_items(self):
        for _ in range(len(self.items)):
            item = self.inspect(self.items.pop(0)) // self.relief

            if item % self.test == 0:
                self.all_monkeys[self.true_monkey].get_item(item)
            else:
                self.all_monkeys[self.false_monkey].get_item(item)
            
            self.items_inspected += 1


def parse_data_to_monkey(data, all_monkeys, relief=1):
    pos = int(data[0].split(':')[0].split(' ')[1])

    items = [int(x) for x in data[1].split(':')[1].split(', ')]
    op = data[2].split('=')[-1]
    test = int(data[3].split(' ')[-1])
    true_monkey = int(data[4].split(' ')[-1])
    false_monkey = int(data[5].split(' ')[-1])

    all_monkeys[pos] = Monkey(items, op, test, true_monkey, false_monkey, all_monkeys, relief)


def part1(monkey_data):
    all_monkeys = [None] * len(monkey_data)

    for monkey in monkey_data:
        parse_data_to_monkey(monkey, all_monkeys, 3)

    for _ in range(10_000):
        for monkey in all_monkeys:
            monkey.inspect_items()

    return prod(sorted([m.items_inspected for m in all_monkeys], reverse=True)[:2])

with open('input.txt') as f:
    monkey_data = [x.split('\n') for x in f.read().split('\n\n')]

print(part1(monkey_data))