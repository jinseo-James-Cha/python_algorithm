class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n < 2:
            return []

        res = []

        def backtrack(target, combination, start):
            for i in range(start, isqrt(target) + 1):
                if target % i == 0:
                    combination.append(i)
                    # i와 (target // i) 두 factor를 바로 결과에 추가
                    res.append(combination + [target // i])
                    backtrack(target // i, combination, i)
                    combination.pop()

        backtrack(n, [], 2)
        return res
