from collections import Counter

books = [input() for _ in range(int(input()))]
counter_bn = Counter(books)

answer = ""
freq = 0
for key, value in counter_bn.items():
    if value > freq:
        answer = key
        freq = value
    elif value == freq and key < answer:
        answer = key

print(answer)