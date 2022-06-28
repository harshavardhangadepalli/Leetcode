# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        s = set()
        s.add(head)
        current = head
        while current.next:
            current = current.next
            if current in s:
                return True
            s.add(current)
        return False