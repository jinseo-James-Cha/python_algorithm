def solution(arr):
    r_len = len(arr)
    c_len = len(arr[0])
    
    if r_len == c_len:
        return arr
    
    is_r_len_bigger = r_len > c_len
    if is_r_len_bigger:
        for i in range(r_len):
            arr[i] += [0] * (r_len - c_len)
    else:
        arr += [[0] * c_len for _ in range(c_len-r_len)]
                
    return arr