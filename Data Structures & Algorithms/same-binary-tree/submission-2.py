# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative DFS
        if not(q or p):
            return True
        
        q1 = deque([p])
        q2 = deque([q])

        while q1 or q2:
            p_node = q1.pop()
            q_node = q2.pop()

            if p_node is None and q_node is None:
                continue

            if (p_node is None and q_node is not None) or (q_node is None and p_node is not None):
                return False

            if p_node.val == q_node.val:
                q1.append(q_node.right)
                q1.append(q_node.left)
                q2.append(p_node.right)
                q2.append(p_node.left)
            else:
                return False

        return True