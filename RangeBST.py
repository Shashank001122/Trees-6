# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi=0
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if root==None:
            return 0
        self.helper(root,L,R)
        return self.maxi
    def helper(self,root,L,R):
        if root==None:
            return
        if root.val>L:
            self.helper(root.left,L,R)
        if root.val<R:
            self.helper(root.right,L,R)
        if root.val>=L and root.val<=R:
            self.maxi+=root.val
        return
        
#Time complexity is O(n)
#Space complexity is O(h)
