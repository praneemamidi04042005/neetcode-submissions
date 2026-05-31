/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    ArrayList<Integer> l=new ArrayList<>();
    public void inorder(TreeNode root){
        if(root==null) return;
        inorder(root.left);
        l.add(root.val);
        inorder(root.right);
    }
    public int rangeSumBST(TreeNode root, int low, int high) {
        inorder(root);
        int c=0;
        for(int i=0;i<l.size();i++){
            if(l.get(i)>=low&&l.get(i)<=high) c+=l.get(i);
        }
        return c;
    }
}