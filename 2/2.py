with open('input.txt') as f:
    rounds = [l.rstrip().split() for l in f.readlines()]

mapping = {
    'rock' : ['A', 'X'],
    'paper' : ['B', 'Y'],
    'scissor' : ['C', 'Z'],
}

def translator(letter):
    for k,v in mapping.items():
        if letter in v:
            return k

score = {
    "rock" : 1,
    "paper" : 2,
    "scissor" :3,
}
winning = {
    "rock" : "paper",
    "paper" : "scissor",
    "scissor" : "rock"
}

sum = 0
for round in rounds:
    opp, you = translator(round[0]), translator(round[1])

    if winning[opp] == you:
        sum += 6
    elif opp == you:
        sum += 3
    sum += score[you]
print(sum)
