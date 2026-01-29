# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # x node is good if in the path from root to x, there is no nodes with greater value

        # root
        # BFS -> and max renewal by level and +1
        countGoodNodes = 0
        queue = deque([(root, root.val)])
        while queue: # (1, 3), (4, 3)
            size = len(queue)
            for _ in range(size):
                curr_node, curr_max = queue.popleft()
                if curr_node.val >= curr_max:
                    countGoodNodes += 1
                
                if curr_node.left:
                    queue.append((curr_node.left, max(curr_max, curr_node.val)))
                
                if curr_node.right:
                    queue.append((curr_node.right, max(curr_max, curr_node.val)))
        return countGoodNodes













        # good node == root -> x there are no nodes with a value greater than X
        #          3
        #       1      4
        # here 3<=     here 4<=
        # keep updating maximum.. and curr val >= maximum count += 1 and reset maximum

        # bfs
        res = 0
        queue = deque([(root, float('-inf'))])
        while queue:
            node, maximum = queue.popleft()
            if node.val >= maximum:
                res += 1
                maximum = node.val
            if node.left:
                queue.append((node.left, maximum))
            if node.right:
                queue.append((node.right, maximum))
        return res


        def dfs(node, maximum):
            nonlocal count
            if not node:
                return

            if node.val >= maximum:
                count += 1
                maximum = node.val

            dfs(node.left, maximum)
            dfs(node.right, maximum)
        
        count = 0
        dfs(root, root.val)
        return count