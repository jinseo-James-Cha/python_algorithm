def solution(n):
#     answer = 0
#     for i in range(1, n + 1):
#         if n % 2 == 0 and i % 2 == 0:
#             answer += i**2
#         elif not n % 2 == 0 and not i % 2 == 0:
#             answer += i
        
#     return answer

# range의 세번째 매개변수는 얼마만큼씩 증가시키는지임. -> "step"
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])