def solution(my_string, indices):
    return ''.join([my_string[i] for i in range(0,len(my_string)) if not i in indices])