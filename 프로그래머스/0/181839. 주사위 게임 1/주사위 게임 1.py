def solution(a, b):
    is_a_odd = a % 2 != 0
    is_b_odd = b % 2 != 0
    
    if is_a_odd and is_b_odd:
        answer = a**2 + b**2
    elif not is_a_odd and not is_b_odd:
        answer = abs(a - b)
    else:
        answer = 2 * (a + b)
    return answer