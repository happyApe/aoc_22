import os

def get_input():
    with open('./input.txt') as f:
        final = [l.rstrip().split() for l in f.readline()]
    with open('./example.txt') as f:
        example = [l.rstrip().split() for l in f.readline()]
    return example, final

def sol(example, final):
    pass

if __name__ == "__main__":
    example, final = get_input()

