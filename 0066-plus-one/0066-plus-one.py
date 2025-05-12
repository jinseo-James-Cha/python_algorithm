class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join([str(a) for a in digits])
        s = str(int(s) + 1)
        answer = [int(a) for a in s]
        return answer
        