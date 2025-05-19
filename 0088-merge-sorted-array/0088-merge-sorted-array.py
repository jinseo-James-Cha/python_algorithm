# my solution 2
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

# put values from the end of nums1 
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m_index = m - 1
        n_index = n - 1
        r_index = len(nums1) - 1

        while m_index >= 0 and n_index >= 0:
            if nums1[m_index] > nums2[n_index]:
                nums1[r_index] = nums1[m_index]
                m_index -= 1
            else:
                nums1[r_index] = nums2[n_index]
                n_index -= 1
            r_index -= 1
        
        while n_index >= 0:
            nums1[r_index] = nums2[n_index]
            r_index -= 1
            n_index -= 1




# my solution 1.
# this is O((m + n) log(m + n))
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         for n in nums2:
#             nums1[m]= n
#             m += 1
#         nums1.sort()