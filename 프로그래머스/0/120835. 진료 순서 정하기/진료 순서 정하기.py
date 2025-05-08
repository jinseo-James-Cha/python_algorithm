def solution(emergency):
    a = sorted(emergency, reverse=True)
    answer = []
    for e in emergency:
        answer.append(a.index(e) + 1)

    return answer