# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        # DFS stack
        # if not root:
        #     return []
        
        # paths = []
        # stack = [(root, str(root.val))]

        # while stack:
        #     node, path = stack.pop()

        #     # if leaf
        #     if not node.left and not node.right:
        #         paths.append(path)
        #     if node.left:
        #         stack.append((node.left, path + '->' + str(node.left.val)))
        #     if node.right:
        #         stack.append((node.right, path + '->' + str(node.right.val)))
        # return paths

        # DFS recursion
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)
        
        paths = []
        construct_paths(root, '')
        return paths