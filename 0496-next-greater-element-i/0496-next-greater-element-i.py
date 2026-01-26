class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []
        for n2 in nums2:
            while stack and n2 > stack[-1]:
                hashmap[stack.pop()] = n2
            stack.append(n2)
        
        res = []
        for n1 in nums1:
            res.append(hashmap.get(n1, -1))
        return res