with open('input.txt') as f:
    rucksacks = [l.rstrip() for l in f.readlines()]


def part1():
    sum = 0
    for rs in rucksacks:
        fhlf = rs[0:len(rs)//2]
        shlf = rs[len(rs)//2 : ]

        common = ''.join(set(fhlf).intersection(shlf))
        if common.isupper():
            sum += ((ord(common.lower())-96) + 26)

        else:
            sum += ((ord(common)-96))

    print(sum)


def part2():
    groups = []
    for i in range(0, len(rucksacks), 3):
        x = i
        groups.append(rucksacks[x:x+3])

    sum = 0
    for g in groups:
        common = ''.join(set.intersection(*map(set, g)))
        if common.isupper():
            sum += ((ord(common.lower())-96) + 26)

        else:
            sum += ((ord(common)-96))
    print(sum)



part2()


