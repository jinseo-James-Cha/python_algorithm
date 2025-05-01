def solution(arr, n):    
    i = int(len(arr) % 2 == 0)
    while i < len(arr):
        arr[i] += n
        i += 2
    
    return arr