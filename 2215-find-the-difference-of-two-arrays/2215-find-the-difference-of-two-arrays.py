class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # a list answer
        # answer[0] ==> distinct integers in nums1 not nums2
        # answer[1] ==> distinct integers in nums2 not nums1

        # set nums1
        # set nums2
        # iterater ...
        answer = [[] for _ in range(2)]
        
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        # nums1 distinct
        for n1 in nums1_set:
            if n1 not in nums2_set:
                answer[0].append(n1)
        
        # nums2 distict
        for n2 in nums2_set:
            if n2 not in nums1_set:
                answer[1].append(n2)
        return answer

        