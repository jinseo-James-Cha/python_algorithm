def solution(age):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    s_age = str(age)
    answer = ''
    for a in s_age:
        answer += alphabets[int(a)]
    return answer