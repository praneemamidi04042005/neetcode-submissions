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
    public ListNode reverseList(ListNode head) {
        ArrayList<Integer> l=new ArrayList<>();
        ListNode p=head;
        while(p!=null){
            l.add(p.val);
            p=p.next;
        }
        Collections.reverse(l);
        p=head;
        int i=0;
        while(p!=null){
            p.val=l.get(i);
            i+=1;
            p=p.next;
        }
        return head;
    }
}
