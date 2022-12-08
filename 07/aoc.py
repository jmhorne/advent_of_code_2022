#!/usr/bin/env python3

class Directory:
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.size = 0
        self.sub_dirs = dict()
        self.files = dict()
    
    def get_size(self):
        sub_size = 0
        for d in self.sub_dirs:
            sub_size += self.sub_dirs[d].get_size()

        return self.size + sub_size
    
    def find_del_size(self, size):
        finds = list()
        sz = self.get_size()

        if sz <= size:
            finds.append(sz)
        
        for d in self.sub_dirs:
            finds += self.sub_dirs[d].find_del_size(size)

        return finds
    
    def find_dir_to_del(self, unused_space):
        finds = list()
        sz = self.get_size()
        if sz + unused_space >= 30_000_000:
            finds.append(sz)
        
        for d in self.sub_dirs:
            finds += self.sub_dirs[d].find_dir_to_del(unused_space)
        
        return finds


with open('input.txt') as f:
    output = [x.split(' ') for x in f.read().split('\n')]

root = Directory(output[0][2])
currDir = root
output.pop(0)

while len(output):
    line = output.pop(0)

    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                currDir = currDir.parent
            elif line[2] not in currDir.sub_dirs:
                currDir.sub_dirs[line[2]] = Directory(line[2], currDir)
                currDir = currDir.sub_dirs[line[2]]
            else:
                currDir = currDir.sub_dirs[line[2]]
        
        elif line[1] == "ls":
            while output[0][0] != "$":
                line = output.pop(0)

                if line[0] == "dir":
                    currDir.sub_dirs[line[1]] = Directory(line[1], currDir)
                else:
                    currDir.files[line[1]] = int(line[0])
                    currDir.size += int(line[0])
                
                if len(output) == 0:
                    break

print(sum(root.find_del_size(100_000)))
print(min(root.find_dir_to_del(70_000_000 - root.get_size())))