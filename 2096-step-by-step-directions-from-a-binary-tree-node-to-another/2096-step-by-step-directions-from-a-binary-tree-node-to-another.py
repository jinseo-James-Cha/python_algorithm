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
        
        lowest ancestor 
        L R
        U - from starting Node to Lowest Ancestor -> only U
        L R - from Lowest Ancestor to destValue -> L or U
        """
        # find Lowest Common Ancestor
        def findAncestor(node, startValue, destValue):
            nonlocal lowestAncestor
            if not node:
                return False
            
            myself = node.val == startValue or node.val == destValue
            leftResult = findAncestor(node.left, startValue, destValue)
            rightResult = findAncestor(node.right, startValue, destValue)

            if myself + leftResult + rightResult >= 2:
                lowestAncestor = node
            
            return myself or leftResult or rightResult

        lowestAncestor = None
        findAncestor(root, startValue, destValue)
        
        if not lowestAncestor:
            return ""

        startPath = ""
        destPath = ""
        foundStart = False
        foundDest = False
        queue = deque([(lowestAncestor, "")])
        while queue:
            curr_node, curr_path = queue.popleft()
            if curr_node.val == startValue:
                startPath = curr_path
                foundStart = True
            elif curr_node.val == destValue:
                destPath = curr_path
                FoundDest = True
            
            if foundStart and foundDest:
                break
            
            if curr_node.left:
                queue.append((curr_node.left, curr_path + "L"))
            
            if curr_node.right:
                queue.append((curr_node.right, curr_path + "R"))

        finalStartPath = "U" * len(startPath)
        return finalStartPath + destPath


