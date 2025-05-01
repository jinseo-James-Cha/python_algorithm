def solution(strArr):
    a = {}
    for s in strArr:
        a[len(s)] = a.get(len(s),0) + 1
        
    # 가장 큰 값의 k를 구하려면...아래와같이?    
    # m = 0
    # answer = 0
    # for k, v in a.items():
    #     if v > m:
    #         answer = k
    return max(a.values())
    