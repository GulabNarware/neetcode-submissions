# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=deque([])
        queue.append(root)
        while len(queue)!=0:
            level=[]
            for i in range(len(queue)):
                a=queue.popleft()
                level.append(a.val)
                if a.left :
                    queue.append(a.left)
                if a.right :
                    queue.append(a.right)
            result.append(level)
        return result


    #     while queue:                 # jab tak nodes hain
    # size = len(queue)        # current level ka size
    # level = []

    # for _ in range(size):    # sirf current level ke nodes
    #     node = queue.popleft()
    #     level.append(node.val)

    #     if node.left:
    #         queue.append(node.left)
    #     if node.right:
    #         queue.append(node.right)

    # result.append(level)     # ek level complete

