# 1 동시에 꺼낼수있다
#    for a,b in queries:

# 2. 동시에 변경할수있다
# arr[a],arr[b]=arr[b],arr[a]

def solution(arr, queries):
    for q in queries:
        temp = arr[q[0]]
        arr[q[0]] = arr[q[1]]
        arr[q[1]] = temp
        
    return arr