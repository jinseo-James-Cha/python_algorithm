def solution(arr, idx):
    answer = -1
    for idx in range(idx, len(arr)):
        if arr[idx]:
            return idx
    return answer