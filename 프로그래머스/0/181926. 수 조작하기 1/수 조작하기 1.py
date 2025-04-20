# control을 리스트로 바꾸고 set을 사용하면 각 레터별 중복의 수를 알수있지않나?
# 아 set으로 하니깐 {'s', 'w', 'a', 'd'} 이렇게 나오네 중복제거만 가능함 + 리스트 아니여도됨

# 정해진 값이 있으면 넣어놓고 바로 서치하는게 빠르지
# 아래와같이
def solution(n, control):
    answer = n
    c = { 'w':1, 's':-1, 'd':10, 'a':-10}
    for i in control:
        answer += c[i]
    return answer

# def solution(n, control):
#     for con in control:
#         if con == 'w':
#             n += 1
#         elif con == 's':
#             n -= 1
#         elif con == 'd':
#             n += 10
#         else:
#             n -= 10
#     return n