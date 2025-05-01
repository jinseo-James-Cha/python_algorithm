def solution(rank, attendance):
    i = 1
    arr = []
    while len(arr) < 3:
        found_i = rank.index(i)
        if attendance[found_i]:
            arr.append(found_i)
        i += 1
    
    return 10000 * arr[0] + 100 * arr[1] + arr[2]