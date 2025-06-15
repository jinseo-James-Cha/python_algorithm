class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = []
        for n1 in nums1:
            for i,n2 in enumerate(nums2):
                if n1 == n2:
                    mapping.append(i)
                    break
        return mapping