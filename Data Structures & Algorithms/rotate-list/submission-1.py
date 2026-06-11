# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        cur=head
        if head==None:
            return head
        while cur:
            l.append(cur.val)
            cur=cur.next
        k%=len(l)
        for i in range(k):
            j=l.pop()
            l.insert(0,j)
        i=0
        cur=head
        while cur:
            cur.val=l[i]
            i+=1
            cur=cur.next
        return head

        