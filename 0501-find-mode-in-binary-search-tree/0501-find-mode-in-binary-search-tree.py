# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # Morris Traversal
        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []

        curr = root
        while curr:
            if curr.left:
                # find the friend
                friend = curr.left
                while friend.right:
                    friend = friend.right
                
                friend.right = curr

                # delete the edge after using it
                left = curr.left
                curr.left = None
                curr = left
            else:
                # Handle the current node
                num = curr.val
                if num == curr_num:
                    curr_streak += 1
                else:
                    curr_streak = 1
                    curr_num = num
                
                if curr_streak > max_streak:
                    ans = []
                    max_streak = curr_streak
                
                if curr_streak == max_streak:
                    ans.append(num)

                # move to right
                curr = curr.right
        return ans

        # it worked, but I didn't use BST well...
        # BST
        # left <= parent <= right
        # Could you do that without using any extra space? 
        # (Assume that the implicit stack space incurred due to recursion does not count).
        # def dfs(node: TreeNode):
        #     if not node:
        #         return
            
        #     hashmap[node.val] += 1
        #     dfs(node.left)
        #     dfs(node.right)

        # hashmap = defaultdict(int)
        # dfs(root)
        
        # max_count = 0
        # res = []
        # for num, cnt in hashmap.items():
        #     if cnt > max_count:
        #         max_count = cnt
        #         res = [num]
        #     elif max_count == cnt:
        #         res.append(num)
        
        # return res

