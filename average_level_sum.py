# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        ans=[]
        q=deque([root])
        while q: 
            l=len(q)
            sum=0
            for i in range(l):
                top=q.popleft()
                sum+=top.val
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            ans.append(sum/l)
        return ans
