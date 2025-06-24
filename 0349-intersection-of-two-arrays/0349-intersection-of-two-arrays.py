class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # unique array... -> set -> list
        res = set()
        s1 = set(nums1)
        s2 = set(nums2)

        for n1 in s1:
            if n1 in s2:
                res.add(n1)
        
        for n2 in s2:
            if n2 in s1:
                res.add(n2)

        return list(res)