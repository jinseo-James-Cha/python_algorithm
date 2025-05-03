def solution(myString):
    return ''.join([a if a > "l" else "l" for a in myString])