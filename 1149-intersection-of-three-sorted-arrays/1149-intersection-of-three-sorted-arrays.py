from collections import defaultdict
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # strictly increasing -> unique nums in asc order
        # 1 <= arr1.length, arr2.length, arr3.length <= 1000 -> meaning all the same length? no

        # 12345     -> 1 2 5
        # 12579     -> 1 5
        # 13458
        # 1   5

        # it means it needs 3 count
        # hashmap -> num and count and make res with 3
        hashmap = defaultdict(int)
        for a1 in arr1:
            hashmap[a1] += 1
        
        for a2 in arr2:
            hashmap[a2] += 1

        res = []
        for a3 in arr3:
            hashmap[a3] += 1
            if hashmap[a3] == 3:
                res.append(a3)
        return res


        