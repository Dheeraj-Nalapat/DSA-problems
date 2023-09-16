# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        t = deque([root])
        if p.val>q.val:
            a1,a2 = q.val,p.val
        else:
            a1,a2 = p.val,q.val    
        while t:
            node = t.popleft()
            if node.val>=a1 and node.val<=a2:
                return node
            if node.left:    
                t.append(node.left) 
            if node.right:
                t.append(node.right)  
