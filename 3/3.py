with open('input.txt') as f:
    rucksacks = [l.rstrip() for l in f.readlines()]


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


