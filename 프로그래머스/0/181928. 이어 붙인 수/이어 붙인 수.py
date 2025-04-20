def solution(num_list):
    even = []
    odd = []
    for num in range(len(num_list)):
        if num_list[num] % 2 == 0:
            even.append(str(num_list[num]))
        else:
            odd.append(str(num_list[num]))
    num_even = int(''.join(even))
    num_odd = int(''.join(odd))
    
    return num_even + num_odd