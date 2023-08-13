#일곱 난쟁이
from itertools import combinations

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

for i in range(len(dwarf)):
    for j in range(i + 1, len(dwarf)):
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
            for k in range(len(dwarf)):
                if k == i or k == j:
                    pass
                else:
                    print(array[k])
            exit()