def solution(myString, pat):
    i = myString.index(pat)
    while True:
        if pat in myString[i+1:]:
            i += 1
        else:
            break
    
    return myString[:i+len(pat)]