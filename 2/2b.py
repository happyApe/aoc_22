with open('input.txt') as f:
    rounds = [l.rstrip().split() for l in f.readlines()]

score = {
    "A" : 1,
    "B" : 2,
    "C" :3,
}

winning = {
    "A" : "B",
    "B" : "C",
    "C" : "A"
}

lose = {
    "A" : "C",
    "B" : "A",
    "C" : "B"
}

sum = 0
for round in rounds:
    opp, you = round[0], round[1]

    if you == "Y":
        sum += (score[opp] + 3)
    elif you == "X": # lose
        sum += (score[lose[opp]])
    else: # win
        sum += (score[winning[opp]] + 6)
print(sum)

        
