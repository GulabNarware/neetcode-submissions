# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(s, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1=[]
        res2=[]

        def ptree(p):
            if not p:
                res1.append("NULL")
                return
            res1.append(p.val)
            ptree(p.left)
            ptree(p.right)

        def qtree(q):
            if not q:
                res2.append("NULL")
                return
            res2.append(q.val)
            qtree(q.left)
            qtree(q.right)
        ptree(p)
        qtree(q)
        if len(res1)!=len(res2):
            return False
        else:
            for i in range(len(res2)):
                if res1[i]!=res2[i]:
                    return False
                    
        return True



