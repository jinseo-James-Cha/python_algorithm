class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = "0" * (len(a)-len(b)) + b
        else:
            a = "0" * (len(b)-len(a)) + a

        toss = False
        i = len(a) - 1
        answer = ""
        while i >= 0:
            int_ab = int(a[i]) + int(b[i]) + int(toss)
            if int_ab == 0:
                temp = "0"
                toss = False
            elif int_ab == 1:
                temp = "1"
                toss = False
            elif int_ab == 2:
                temp = "0"
                toss = True
            else:
                temp = "1"
                toss = True
            answer = temp + answer
            i -= 1

        if toss:
            answer = "1" + answer
        
        return answer