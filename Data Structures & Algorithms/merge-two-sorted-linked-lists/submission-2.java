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
    ListNode head=null;
    public void insert(int d){
        ListNode newnode=new ListNode(d);
        if(head==null){head=newnode;return;}
        ListNode cur=head;
        while(cur.next!=null) cur=cur.next;
        cur.next=newnode;
    }
     ArrayList<Integer> l=new ArrayList<>();
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode cur=list1;
        while(cur!=null){
            l.add(cur.val);
            cur=cur.next;
        }
        cur=list2;
        while(cur!=null){
            l.add(cur.val);
            cur=cur.next;
        }
        Collections.sort(l);
        for(int i=0;i<l.size();i++){
            insert(l.get(i));
        }
        return head;
    }
}