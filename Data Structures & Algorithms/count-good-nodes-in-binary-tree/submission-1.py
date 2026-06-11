# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count=0
        def dfs(root,v):
            if not root:
                return 
            if root.val>=v:
                self.count+=1
            v=max(root.val,v)
            dfs(root.left,v)
            dfs(root.right,v)
            return 
        dfs(root,root.val)
        return self.count
