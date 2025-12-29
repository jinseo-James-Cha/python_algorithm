# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        this is quite difficult for me, so I want to understand properly.

        I am using DFS and Prefix-Sum algorithms

        if not node return 

        curr_sum is the prefix sum
        curr_sum + curr_node.val ==> curr_prefix_sum == targetSum -> found one path -> count += 1
        
        if curr_prefix_sum - targetSum is in hashmap means there is sub path is matching..
        like prefix[j] - prefix[i] => i~j sum,,
        ts = prefix[j] - prefix[i]
        prefix[i] = prefix[j] - ts

        and then
        register its curr_prefix_sum into hashmap
        
        and traversal as preorder, parent -> left -> right
        after children traversal, remove the path => h[curr_sum] -= 1
        """
        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return
            
            curr_sum += node.val
            if curr_sum == ts:
                count += 1
            
            count += h[curr_sum - ts]

            h[curr_sum] += 1
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            h[curr_sum] -= 1

        count = 0
        ts = targetSum
        h = defaultdict(int)
        preorder(root, 0)
        return count


        