# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        arr=[]
        p=head
        while p:
            arr.append(p)
            p=p.next
        
        l,r=0,len(arr)-1

        head=arr[l]
        while l<r:
            arr[l].next=arr[r]
            l+=1
            if l>=r:
                break

            arr[r].next=arr[l]
            r-=1
        arr[l].next=None
       
            