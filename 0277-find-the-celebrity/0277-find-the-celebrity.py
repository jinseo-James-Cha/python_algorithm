# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        0 ~ n -1
        n = 3
        0, 1 ,2
        """
        for i in range(n):
            found = True
            for j in range(n):
                if i == j:
                    continue

                if knows(i, j) or not knows(j, i):
                    found = False
                    break
            if found:
                return i
        return -1