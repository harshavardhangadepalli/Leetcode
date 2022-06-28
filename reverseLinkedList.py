# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        d = dict()
        d[0] = head
        i = 1
        while head.next:
            d[i] = head.next
            head = head.next
            i+=1
        head = d[i-1]
        ptr = head
        for x in range(i-1)[::-1]:
            ptr.next = d[x]
            ptr = ptr.next
        ptr.next = None
        return(head)