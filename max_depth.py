# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)

        return 1+max(l,r)
def main():
   
   root = [3,9,20,None,None,15,7]

if __name__ == '__main__':
  main()

