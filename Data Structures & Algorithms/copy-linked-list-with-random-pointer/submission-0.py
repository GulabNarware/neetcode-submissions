"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic={None:None}

        point=head
        while point:
            copy=Node(point.val)
            dic[point]=copy
            point=point.next

        point=head
        while point:
            copy=dic[point]
            copy.next=dic[point.next]
            copy.random=dic[point.random]
            point=point.next
        return dic[head]

            
