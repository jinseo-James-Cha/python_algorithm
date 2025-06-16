# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        # yes ! I like Tree question
        # node.val -> lowercase English letters (possibly empty)
        # node.len -> non-negative integer

        # types
        # leaf : no children, len = 0, val is non-empty string
        # internal: 1 or 2 children, len > 0, val is empty

        # S[node]
        # if leaf, S[node] = node.val
        # it not, S[node] = concat(S[node.left], S[node.right]) and S[node].length = node.len
        
        # return k-th character of string S[root]

        # implement all logic and then return value

        # I think this solution is not what they want to see
        # I should have used the root.len for backtracking
        # DFS will be useful to get leaves
        # S = ""
        def dfs(root: Optional[object]):
            if not root:
                return ""

            if root.len == 0 and root.val:
                return root.val
            
            return dfs(root.left) + dfs(root.right)
            
        S = dfs(root)
        return S[k-1]

