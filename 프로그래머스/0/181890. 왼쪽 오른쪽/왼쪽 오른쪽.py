def solution(str_list):
    answer = []
    
    if "l" in str_list and "r" in str_list:
        i_index = str_list.index("l")
        r_index = str_list.index("r")
        if i_index < r_index:
            answer = str_list[:i_index]
        else:
            answer = str_list[r_index + 1:]
    elif "l" in str_list:
        i_index = str_list.index("l")
        answer = str_list[:i_index]
    elif "r" in str_list:
        r_index = str_list.index("r")
        answer = str_list[r_index + 1:]
    
    return answer