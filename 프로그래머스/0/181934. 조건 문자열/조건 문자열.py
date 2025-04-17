def solution(ineq, eq, n, m):
    # version 1
    # if ineq == '<':
    #     if eq == '=':
    #         return int(n <= m)
    #     else:
    #         return int(n < m)
    # else:
    #     if eq == '=':
    #         return int(n >= m)
    #     else:
    #         return int(n > m)
    
    # version 2
    # if eq == '!':
    #     return int(n > m) if ineq == '>' else int(n < m)
    # else:
    #     return int(n >= m) if ineq == '>' else int(n <= m)
    
    # version 3
    eq = eq if eq == '=' else ''
    return int(eval(f"{n} {ineq}{eq} {m}"))