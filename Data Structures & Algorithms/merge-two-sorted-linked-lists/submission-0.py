# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1=list1
        if p1==None:
            p1=list2
            return p1
        while p1.next!=None:
            p1=p1.next
        p1.next=list2
        p1=list1
        l=[]
        while p1.next!=None:
            l.append(p1.val)
            p1=p1.next
        l.append(p1.val)
        l.sort()
        i=0
        p1=list1
        while p1.next!=None:
            p1.val=l[i]
            i+=1
            p1=p1.next
        p1.val=l[i]
        return list1
        