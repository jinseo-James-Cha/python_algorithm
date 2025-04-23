# version 2
# Counter없이 그냥 map을 써보자 pure하게!
# map == dict
books = dict()
for _ in range(int(input())):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

max_num = max(books.values())
candi = []
for key, value in books.items():
    if max_num == value:
        candi.append(key)

candi.sort()
print(candi[0])

# version 1 using Counter

# from collections import Counter

# books = [input() for _ in range(int(input()))]
# counter_bn = Counter(books)

# answer = ""
# freq = 0
# for key, value in counter_bn.items():
#     if value > freq:
#         answer = key
#         freq = value
#     elif value == freq and key < answer:
#         answer = key

# print(answer)