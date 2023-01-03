import os

def get_input():
    with open('./input.txt') as f:
        inp = [l.rstrip().split() for l in f.readlines()]
    return inp[0][0]

def part1(inp):
    uniq = ""
    i = 0
    for char in inp:
        if len(uniq) == 4:
            print(i)
            print(uniq)
            break
        while char in uniq:
            uniq = uniq[1:]
        uniq+=char
        i+=1

def part2(inp):
    uniq = ""
    i = 0
    for char in inp:
        if len(uniq) == 14 : #or len(uniq) >= len(inp):
            print(i)
            print(uniq)
            break
        while char in uniq:
            uniq = uniq[1:]
        uniq+=char
        i+=1

if __name__ == "__main__":
    inp = get_input()

    part1(inp)
    part2(inp)

