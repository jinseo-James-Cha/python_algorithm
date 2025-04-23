from itertools import combinations

heights = [int(input()) for _ in range(9)]
heights.sort()

for i in combinations(heights, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break