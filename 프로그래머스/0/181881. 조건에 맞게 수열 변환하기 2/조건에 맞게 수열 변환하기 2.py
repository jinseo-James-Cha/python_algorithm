def solution(arr):
    answer = 0
    flag = True
    while flag:
        temp = arr.copy()
        for i, num in enumerate(arr):
            if num >= 50 and num % 2 == 0:
                arr[i] = num / 2
            elif num < 50 and not num % 2 == 0:
                arr[i] = num * 2 + 1
        
        if temp == arr:
            flag = False
        else:
            answer += 1
        
    return answer