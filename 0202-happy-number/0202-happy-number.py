class Solution:
    def isHappy(self, n: int) -> bool:
        # repeat the process until the number equals 1 -> happy
        # or it loops endlessly in a cycle without 1
        # so 1 or endless
        # add num in to set
        # if its in, then return false
        # if not, keep checking
        seen = set()
        while n > 1:
            if n in seen:
                return False
            else:
                seen.add(n)

            temp = 0
            for num in str(n):
                temp += int(num) ** 2
            n = temp

        return True













# how can we think its fast and slow pointers..
# there are two cases
# 1. final number 1 -> True
# 2. loops endlessly in a cycle -> False

# Floy'd cycle detection algorithm
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         def getNextNum(num: int) -> int:
#             nextNum = 0
#             while num > 0:
#                 nextNum += (num % 10)**2                
#                 num //= 10
#             return nextNum

#         slow = fast = n
#         while fast != 1:
#             slow = getNextNum(slow)
#             fast = getNextNum(getNextNum(fast))
#             if slow == fast:
#                 return False
#         return True