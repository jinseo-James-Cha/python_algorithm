# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def binary_search(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            curr = TreeNode(nums[mid])
            curr.left = binary_search(left, mid-1)
            curr.right = binary_search(mid+1, right)
            return curr

        return binary_search(0, len(nums)-1)