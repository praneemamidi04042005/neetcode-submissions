# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        p=head
        while p!=None:
            l.append(p.val)
            p=p.next
        for i in range(0,len(l)-k+1,k):
            l[i:i+k]=l[i:i+k][::-1]
        p=head
        i=0
        while p!=None:
            p.val=l[i]
            i+=1
            p=p.next
        return head
        