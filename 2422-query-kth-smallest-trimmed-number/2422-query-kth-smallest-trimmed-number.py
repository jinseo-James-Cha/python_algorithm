class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        # equal length, only digits str
        # queries = [k, trim] rightmost trim digit
        answer = []
        for k, trim in queries:
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            trimmed.sort()
            answer.append(trimmed[k-1][1])
        return answer


