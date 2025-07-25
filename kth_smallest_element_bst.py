# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values=[]

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        inorder(root)
        return values[k-1]
