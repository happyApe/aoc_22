import heapq
with open('input.txt') as f:
    elf_cal = []
    sumish = 0
    for line in f:
        if line == '\n':
            elf_cal.append(sumish)
            sumish = 0
        else:
            sumish += int(line)
    # print(max(elf_cal))
    heapq.heapify(elf_cal)
    elf_cal = heapq.nlargest(3, elf_cal)
    print(sum(elf_cal))

