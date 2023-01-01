import os

def get_input():
    with open('./input.txt') as f:
        inp = [l.strip().split(',') for l in f.readlines()]
    return inp

def range_cal(pair):
    l = int(pair.split('-')[0])
    h = int(pair.split('-')[-1])
    return set(range(l,h+1))


def part1(inp):
    count = 0
    for pair in inp:
        elf1 = range_cal(pair[0])
        elf2 = range_cal(pair[1])

        if len(elf1 & elf2)==len(elf1) or len(elf1 & elf2)==len(elf2):
            count+=1

    print(count)
def part2(inp):
    count = 0
    for pair in inp:
        elf1 = range_cal(pair[0])
        elf2 = range_cal(pair[1])
        
        if len(elf1 & elf2) > 0:
            count+=1
    print(count)
    

if __name__ == "__main__":
    inp = get_input()

    part1(inp)
    part2(inp)

