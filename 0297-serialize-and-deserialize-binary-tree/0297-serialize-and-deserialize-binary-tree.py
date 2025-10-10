# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            # check base case
            if root is None:
                string += 'None,'
            else:
                # preorder
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string

        return rserialize(root, '')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(q):
            """ a recursive helper function for deserialization."""
            if q[0] == 'None':
                q.popleft()
                return None
                
            node = TreeNode(int(q.popleft()))
            node.left = rdeserialize(q)
            node.right = rdeserialize(q)
            return node

        queue = deque(data.split(','))
        root = rdeserialize(queue)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))