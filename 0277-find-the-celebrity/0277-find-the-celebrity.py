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
        # greedy
        def is_celebrity(i):
            for j in range(n):
                if i == j: continue
                if knows(i,j) or not knows(j,i):
                    return False
            return True

        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        if is_celebrity(candidate):
            return candidate
        return -1

        # brute force -> o(n^2)
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