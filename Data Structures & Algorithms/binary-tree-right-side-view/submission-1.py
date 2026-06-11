# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

#-----------------------------------------------------------------------------
#         if not root:
#             return []

#         res=[]

#         queue=collections.deque()
#         queue.append(root)

#         while queue:

#             level=[]

#             for i in range(len(queue)):
#                 node=queue.popleft()
#                 level.append(node.val)


#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(level)
#         ans=[]
#         for i in res:
#             ans.append(i[-1])
            
#         return ans

#-----------------------------------------------------------------------------
        res=[]
        q=deque([root])

        while q:
            rightside=None
            qlen=len(q)

            for i in range(qlen):
                node=q.popleft()
                if node:
                    rightside=node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val)   
        return res                 