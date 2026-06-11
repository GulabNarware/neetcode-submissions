# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root ==None:
                return [True,0]
            
            left=height(root.left)
            right=height(root.right)

            value=left[1]-right[1]
            if value<0:
                value=(-value)

            balance=(left[0]and right[0] and value<=1)

            return [balance,1+left[1]if left[1]>right[1]else 1+right[1]]

        return height(root)[0]




