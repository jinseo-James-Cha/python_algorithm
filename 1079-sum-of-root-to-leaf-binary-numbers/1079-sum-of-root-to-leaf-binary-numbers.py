# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # preorder
        res = 0
        stack = [(root, 0)]

        while stack:
            root, curr_number = stack.pop()
            if root is not None:
                curr_number = (curr_number << 1) | root.val # 기존 숫자를 왼쪽으로 밀고, 현재 노드 값을 맨 오른쪽 자리에 붙이는 것과 같다!
                if root.left is None and root.right is None:
                    res += curr_number
                else:
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))
        return res
        