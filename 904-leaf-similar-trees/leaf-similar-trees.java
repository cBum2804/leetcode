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

    public ArrayList<Integer> storeLeaves(TreeNode root, ArrayList<Integer> leaf){
        if(root == null){
            return leaf;
        }
        if(root.left==null && root.right == null){
            leaf.add(root.val);
        } 

        leaf =  storeLeaves(root.left, leaf);
        leaf = storeLeaves(root.right, leaf);

        return leaf;
    }
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> tree1 = new ArrayList<>();
        tree1 = storeLeaves(root1, tree1);

        ArrayList<Integer> tree2 = new ArrayList<>();
        tree2 = storeLeaves(root2, tree2);

        return tree1.equals(tree2);
    }
}