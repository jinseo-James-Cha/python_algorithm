from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        n = num of nodes
        node values are unique 1 ~ n

        startValue -> starting node's value
        destValue -> ending node's value

        shortest path from start node to dest value
        
        lowest ancester 
        L R
        U - from starting Node to Lowest Ancester -> only U
        L R - from Lowest Ancester to destValue -> L or U
        """
        # find Lowest Ancester
        def findAncester(node, startValue, destValue):
            nonlocal lowestAncester
            if not node:
                return False
            
            myself = node.val == startValue or node.val == destValue
            leftResult = findAncester(node.left, startValue, destValue)
            rightResult = findAncester(node.right, startValue, destValue)

            if myself + leftResult + rightResult >= 2:
                lowestAncester = node
            
            return myself or leftResult or rightResult

        lowestAncester = None
        findAncester(root, startValue, destValue)
        

        startPath = ""
        destPath = ""
        queue = deque([(lowestAncester, "")])
        while queue:
            curr_node, curr_path = queue.popleft()
            if curr_node.val == startValue:
                startPath = curr_path
            elif curr_node.val == destValue:
                destPath = curr_path
            
            if startPath and destPath:
                break
            
            if curr_node.left:
                queue.append((curr_node.left, curr_path + "L"))
            
            if curr_node.right:
                queue.append((curr_node.right, curr_path + "R"))

        finalStartPath = "U" * len(startPath)
        return finalStartPath + destPath


