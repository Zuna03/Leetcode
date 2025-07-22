# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ltr=1
        q=deque([root])
        ans=[]
        while q:
            l=len(q)
            temp=[]
            for i in range(l):
                node=q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not ltr:
                temp.reverse()
            ans.append(temp)
            ltr=not ltr
        return ans
