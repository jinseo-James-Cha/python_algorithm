# 답지에 외워둘만한 두가지.
# try:
#   ...
# except:
#   ...
# index(찾는값, 시작index)

def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer

## 내가 푼 방식이고 
def solution(arr, idx):
    answer = -1
    for idx in range(idx, len(arr)):
        if arr[idx]:
            return idx
    return answer