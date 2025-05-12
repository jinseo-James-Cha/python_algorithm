def solution(numbers, k):
    answer = 0
    l = len(numbers) 
    
    while l < (k - 1) * 2 + 1:
        numbers += numbers
        l = len(numbers) 
    
    index = (k - 1) * 2
    return numbers[index]