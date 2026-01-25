class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        # Pointers for nums1 (end of actual elements), nums2, and final position
        p1, p2, p = m - 1, n - 1, m + n - 1

        # While there are elements to compare in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If elements remain in nums2, copy them over
        # (nums1 remaining elements are already in place)
        nums1[:p2 + 1] = nums2[:p2 + 1]




        # nums1_copy = nums1[:m]

        # p1, p2 = 0, 0
        # for i in range(m+n):
        #     if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
        #         nums1[i] = nums1_copy[p1]
        #         p1 += 1
        #     else:
        #         nums1[i] = nums2[p2]
        #         p2 += 1