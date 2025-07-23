# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mini=float('inf')
        self.prev=None
        def calc(node):
            if not node:
                return 
            calc(node.left)
            if self.prev is not None:
                self.mini=min(self.mini,abs(node.val-self.prev))
            self.prev=node.val
            calc(node.right)
            
        calc(root)
        return self.mini