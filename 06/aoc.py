#!/usr/bin/env python3

def find_marker(datastream:str, msglen:int):
    charsProcessed = msglen
    buffer = datastream[:msglen]
    while len(set(buffer)) != msglen:
        buffer = buffer[1:] + datastream[charsProcessed]
        charsProcessed += 1
    
    return charsProcessed

if __name__ == '__main__':
    with open('input.txt') as f:
        datastream = f.read()
    
    print(find_marker(datastream, 4))
    print(find_marker(datastream, 14))
