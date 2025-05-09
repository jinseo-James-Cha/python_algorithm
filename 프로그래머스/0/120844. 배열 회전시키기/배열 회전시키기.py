# def solution(numbers, direction):
#     answer = []
#     if direction == "right":
#         answer.append(numbers[-1])
#         answer += numbers[:len(numbers)-1]
#     else:
#         answer += numbers[1:]
#         answer.append(numbers[0])
        
#     return answer

# VERSION 2
# using deque
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers) # make list -> deque
    if direction == 'right':
        numbers.rotate(1) # simply done by this function.
    else:
        numbers.rotate(-1) # simply done by this function.
    return list(numbers)

# VERSION 3
# using deque
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        a = numbers.pop()
        numbers.appendleft(a)
    else:
        a = numbers.popleft()
        numbers.append(a)
    return list(numbers)
