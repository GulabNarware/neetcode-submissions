# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def preord(root):
            if not root:
                return
            res.append(root.val)
            preord(root.left)
            preord(root.right)
        preord(root)
        return res
        