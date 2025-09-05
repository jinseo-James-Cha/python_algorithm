# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # morris traversal
        res = []
        curr = root
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr = curr.right
            else:
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                
                # connect prede -> curr
                if predecessor.right is None:
                    predecessor.right = curr
                    curr = curr.left
                else: # disconnect predecessor -> curr
                    predecessor.right = None
                    res.append(curr.val)
                    curr = curr.right
        return res












        # Morris Traversal
        res = []
        current = root
        while current:
            if current.left is None:
                res.append(current.val)
                # visit
                current = current.right 
            else:
                # next target
                predecessor = current.left 
                # move to left's rightmost node
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                # first visit -> create link(thread)
                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else: # second visit -> remove link and get value
                # 나의 왼쪽 섭트리의 맨 오른쪽 노드가 바로 나야 ! -> 나를 방문하고 오른쪽으로가 
                    predecessor.right = None
                    res.append(current.val)
                    current = current.right
        return res

        # res = [] 
        # stack = []
        # curr = root

        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left

        #     curr = stack.pop()
        #     res.append(curr.val)
        #     curr = curr.right
        
        # return res



# try # 1 recursive
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         # YES BT problem.
#         # inorder

#         res = [] 
#         # go left -> root (myself) -> go right
#         def inorder(root):
#             if not root:
#                 return
#             inorder(root.left)
#             res.append(root.val)
#             inorder(root.right)
        
#         inorder(root)
#         return res
        
            