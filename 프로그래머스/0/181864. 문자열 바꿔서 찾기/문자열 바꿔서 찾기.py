def solution(myString, pat):
    yourString = ''.join(["A" if a == "B" else "B" for a in myString])
    return int(pat in yourString)