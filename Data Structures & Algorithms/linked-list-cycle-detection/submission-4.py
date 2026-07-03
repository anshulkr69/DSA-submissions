# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        if not slow:
            return False
        while fast.next:
            if slow.next == fast.next.next:
                return True
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else:
                return False
        return False