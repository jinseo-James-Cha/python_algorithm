# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
    
        def dfs(node, curr):
            if not node.left and not node.right:
                total.append(curr+node.val)
                return
            
            if node.left:
                dfs(node.left, (curr+node.val) * 10)
            
            if node.right:
                dfs(node.right, (curr+node.val) * 10)
	

        total = []
        dfs(root, 0)
        return sum(total)












        # Morris preorder
        # root_to_leaf = curr_number = 0

        # curr = root
        # while curr:
        #     if curr.left is None:
        #         curr_number = curr_number * 10 + curr.val
        #         if curr.right is None:
        #             root_to_leaf += curr_number
        #         curr = curr.right
        #     else:
        #         predecessor = curr.left
        #         steps = 1
        #         while predecessor.right and predecessor.right != curr:
        #             predecessor = predecessor.right
        #             steps += 1
                
        #         if predecessor.right is None:
        #             curr_number = curr_number * 10 + curr.val
        #             predecessor.right = curr
        #             curr = curr.left
        #         else:
        #             if predecessor.left is None:
        #                 root_to_leaf += curr_number

        #             for _ in range(steps):
        #                 curr_number //= 10
        #             predecessor.right = None
        #             curr = curr.right
            
        # return root_to_leaf



        # bfs
        root_to_leaf = 0
        queue = [(root, 0)]
        while queue:
            curr_node, curr_total = queue.pop()
            if curr_node is not None:
                curr_total = curr_total * 10 + curr_node.val
                if curr_node.left is None and curr_node.right is None:
                    root_to_leaf += curr_total
                else:
                    queue.append((curr_node.left, curr_total))
                    queue.append((curr_node.right, curr_total))
            
        return root_to_leaf



        
        # dfs
        def dfs(node, totalSum):
            if not node:
                return 0

            if not node.left and not node.right:
                return totalSum*10 + node.val

            totalSum = totalSum*10 + node.val
            return dfs(node.left, totalSum) + dfs(node.right, totalSum)
                
        return dfs(root, 0)