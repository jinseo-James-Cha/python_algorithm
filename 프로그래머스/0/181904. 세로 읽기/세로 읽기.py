def solution(my_string, m, c):
    # answer = ''
    # for st in my_string[c-1::m]:
    #     answer += st
    
    return ''.join([st for st in my_string[c-1::m]])