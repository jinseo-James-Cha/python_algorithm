from bisect import bisect_left, bisect_right

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        is_num1_small = len(nums1) < len(nums2)
        if not is_num1_small:
            nums1, nums2 = nums2, nums1
            
        answer = []
        for i in range(len(nums1)):
            if nums1[i] in answer:
                continue
            elif nums1[i] in nums2:
                n1_count = bisect_right(nums1, nums1[i]) - bisect_left(nums1, nums1[i])
                n2_count = bisect_right(nums2, nums1[i]) - bisect_left(nums2, nums1[i])
                answer += [nums1[i]] * min(n1_count, n2_count)
                
        return answer