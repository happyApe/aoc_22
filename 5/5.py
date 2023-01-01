import os

def stack_creator(levels):
    *crates,numstacks = levels.split('\n')
    num_stacks = len(numstacks.split())
    stacks = [[] for _ in range(num_stacks)]
    crates.reverse()
    for crate in crates:
        for stack_idx, i in enumerate(range(1, len(crates[0]), 4)): # 4 is the step to get the next character
            if crate[i].strip():
                stacks[stack_idx].append(crate[i])
    return stacks

def parse(instr):
    instr = instr.split(' ')
    num_crates, initial, final = instr[1], instr[3], instr[-1]
    return int(num_crates), int(initial)-1, int(final)-1

def get_input():
    with open('./input.txt') as f:
        levels, instructions = f.read().split('\n\n')
        stacks  = stack_creator(levels)
    return stacks, instructions.split('\n')[:-1]
    

def part1(stacks, instructions):
    for instr in instructions:
        n, i, f = parse(instr)
        for _ in range(n):
            stacks[f].append(stacks[i].pop())
    [print(stack[-1], end="") for stack in stacks]





def part2(inp):
    pass

if __name__ == "__main__":
    inp = get_input()

    part1(inp[0],inp[1])
    # part2(inp)

