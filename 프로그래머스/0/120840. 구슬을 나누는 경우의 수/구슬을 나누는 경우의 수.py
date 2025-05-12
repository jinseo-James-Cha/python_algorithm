
def solution(balls, share):
    if share > balls:
        return 0
    num = 1 
    denom = 1  

    for i in range(share):
        num *= balls - i
        denom *= i + 1

    return num // denom
