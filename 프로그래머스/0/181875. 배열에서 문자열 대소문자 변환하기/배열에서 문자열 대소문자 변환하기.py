def solution(strArr):
    for i,x in enumerate(strArr):
        if i % 2 == 0:
            strArr[i] = x.lower()
        else:
            strArr[i] = x.upper()
    return strArr