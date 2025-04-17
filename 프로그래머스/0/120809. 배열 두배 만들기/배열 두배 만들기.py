def solution(numbers):
    # version 1
    # answer = []
    # for number in numbers:
    #     answer.append(number * 2)
    # return answer
    
    # version 2 - list comprehension
    return [number * 2 for number in numbers]