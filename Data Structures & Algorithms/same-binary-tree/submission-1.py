# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive DFS
        if p is None and q is None:
            return True
        
        if (p is None and q is not None) or (q is None and p is not None):
            return False
        
        if not self.isSameTree(p.right, q.right):
            return False
        
        if not self.isSameTree(p.left, q.left):
            return False

        if p.val == q.val:
            return True
        else:
            return False
        