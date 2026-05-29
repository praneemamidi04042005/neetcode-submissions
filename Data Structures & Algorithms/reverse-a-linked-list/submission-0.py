# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        p=head
        if head==None:
            return head
        while p.next!=None:
            l.append(p.val)
            p=p.next
        l.append(p.val)
        l=l[::-1]
        i=0
        p=head
        while p.next!=None:
            p.val=l[i]
            i+=1
            p=p.next
        p.val=l[i]
        return head

        