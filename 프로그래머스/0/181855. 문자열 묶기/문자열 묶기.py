def solution(strArr):
    answer = 0
    a = {}
    for s in strArr:
        a[len(s)] = a.get(len(s),0) + 1
    
    m = 0
    for k, v in a.items():
        if v > m:
            m = v
    return m