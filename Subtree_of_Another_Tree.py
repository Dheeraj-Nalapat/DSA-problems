# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        else:
            if not self.sameTree(root,subRoot):
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            else:
                return True            
 
    def sameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        else:
            return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right) 
