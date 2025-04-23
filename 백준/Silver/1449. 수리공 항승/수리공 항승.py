
N, L = map(int, input().split())
places = list(map(int, input().split()))
places.sort()

ct = 0
i = 0
while i < len(places):
    ct += 1
    end_of_tape = places[i] + L
    
    i += 1
    while i < len(places) and end_of_tape > places[i]:
        i += 1

print(ct)