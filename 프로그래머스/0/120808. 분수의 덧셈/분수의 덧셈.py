def solution(numer1, denom1, numer2, denom2):
    new_numer = (numer1 * denom2) + (numer2 * denom1)
    new_denom = denom1 * denom2
    
    # GCD = Greatest Common Divisor
    answer = [new_numer , new_denom]
    for i in range(min(new_numer, new_denom), 1, -1):
        if new_numer % i == 0 and new_denom % i == 0:
            answer = [new_numer / i, new_denom / i]
            break
    
    return answer
