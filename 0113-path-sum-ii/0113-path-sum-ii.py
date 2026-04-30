# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # BFS
        if not root:
            return []
        
        res = []
        queue = deque([(root, [], targetSum)])
        while queue:
            curr_node, curr_combo, remaining = queue.popleft()
            curr_combo.append(curr_node.val)
            if remaining == curr_node.val and not curr_node.left and not curr_node.right:
                res.append(curr_combo[:])
                continue
            
            if curr_node.left:
                queue.append((curr_node.left, curr_combo[:], remaining - curr_node.val))
            
            if curr_node.right:
                queue.append((curr_node.right, curr_combo[:], remaining - curr_node.val))
        return res


        # DFS
        def dfs(node, curr, remaining):
            nonlocal res
            if not node:
                return
            
            curr.append(node.val)
            if remaining == node.val and not node.left and not node.right:
                res.append(curr[:])
            else:
                if node.left:
                    dfs(node.left, curr, remaining - node.val)
                
                if node.right:
                    dfs(node.right, curr, remaining - node.val)
            curr.pop()

        res = []
        dfs(root, [], targetSum)
        return res
            