def solution(intStrs, k, s, l):
    answer = []
    for intS in intStrs:
        x = int(intS[s: s+l])
        if x > k:
            answer.append(x)
    return answer