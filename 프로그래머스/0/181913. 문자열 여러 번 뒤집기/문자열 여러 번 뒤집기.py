def solution(my_string, queries):
    for start, end in queries:
        first_part = my_string[0:start] 
        reverse_part = ""
        for i in range(end, start-1, -1):
            reverse_part += my_string[i]
        last_part = my_string[end+1: len(my_string)] 
        
        my_string = first_part + reverse_part + last_part
    return my_string