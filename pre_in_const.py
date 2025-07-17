# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_val=preorder[0]
        root=TreeNode(root_val)
        idx=inorder.index(root_val)
        left_in=inorder[:idx]
        right_in=inorder[idx+1:]
        left_pre=preorder[1:1+len(left_in)]
        right_pre=preorder[1+len(left_in):]

        root.left=self.buildTree(left_pre,left_in)
        root.right=self.buildTree(right_pre,right_in)

        return root