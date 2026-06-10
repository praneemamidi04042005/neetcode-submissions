/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode p=head;
        int c=0;
        while(p!=null){
            c+=1;
            p=p.next;
        }
        if(head==null) return null;
        if(c==n) return head.next;
        int res=c-n;
        p=head;
        while(p!=null){
            res--;
            if(res==0) break;
            p=p.next;
        }
        p.next=p.next.next;
        return head;
    }
}
