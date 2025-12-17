class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # n kids with candies
        # candies[i] -> ith kid's candies
        res = [False] * len(candies)
        max_candy = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                res[i] = True
        return res