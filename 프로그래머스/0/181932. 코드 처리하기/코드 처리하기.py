# mode -> 0 , 1
# read code from index 0 to len(code - 1) by 1 step

def solution(code):
    answer = []
    mode = 0
    for idx in range(0, len(code)):
        if mode == 0:
            if not code[idx] == "1" and idx % 2 == 0:
                answer.append(code[idx])
            elif code[idx] == "1":
                mode = 1
        else:
            if not code[idx] == "1" and not idx % 2 == 0:
                answer.append(code[idx])
            elif code[idx] == "1":
                mode = 0
    return ''.join(answer) if answer else "EMPTY"