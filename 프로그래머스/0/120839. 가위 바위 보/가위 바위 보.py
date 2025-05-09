# s = 2 / r = 0 / p = 5
def solution(rsp):
    hm = {"2": "0", "0": "5", "5": "2"}
    return ''.join([hm.get(a) for a in rsp])