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
    ListNode head1=null;
    public void insert(int val){
        ListNode newnode=new ListNode(val);
        if(head1==null){head1=newnode;return;}
        ListNode cur=head1;
        while(cur.next!=null) cur=cur.next;
        cur.next=newnode;
    }
    public ListNode removeElements(ListNode head, int val) {
        ListNode cur=head;
        while(cur!=null){
            if(cur.val!=val) insert(cur.val);
            cur=cur.next;
        }
        return head1;
    }
}