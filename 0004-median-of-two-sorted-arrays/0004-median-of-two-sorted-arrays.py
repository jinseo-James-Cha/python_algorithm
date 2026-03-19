class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force
        # merge the list and then get the middle

        merged_list = []
        num1_idx, num2_idx = 0, 0
        while num1_idx < len(nums1) or num2_idx < len(nums2):
            curr_num1 = nums1[num1_idx] if num1_idx < len(nums1) else float('inf')
            curr_num2 = nums2[num2_idx] if num2_idx < len(nums2) else float('inf')

            if curr_num1 < curr_num2:
                merged_list.append(curr_num1)
                num1_idx += 1
            elif curr_num1 > curr_num2:
                merged_list.append(curr_num2)
                num2_idx += 1
            else:
                merged_list.append(curr_num1)
                merged_list.append(curr_num2)
                num1_idx += 1
                num2_idx += 1
        
        is_odd = False if len(merged_list) % 2 == 0 else True
        if is_odd:
            return float(merged_list[len(merged_list) // 2])
        
        return float((merged_list[len(merged_list) // 2] + merged_list[len(merged_list) // 2 - 1]) / 2)




