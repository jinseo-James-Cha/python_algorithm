# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # dfs + prefix sum with the path sum in hashmap + count
        def dfs(node, prefix_sum):
            nonlocal path_count
            if not node:
                return
            
            total_sum = prefix_sum + node.val
            if total_sum == ts:
                path_count += 1
            path_count += hashmap[total_sum - ts]
            
            hashmap[total_sum] += 1
            dfs(node.left, total_sum)
            dfs(node.right, total_sum)

            # take back the node.val when it is done
            hashmap[total_sum] -= 1


        ts = targetSum
        hashmap = defaultdict(int)
        path_count = 0
        dfs(root, 0)
        return path_count

