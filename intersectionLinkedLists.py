# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        ptr1 = headA
        ptr2 = headB
        while ptr1:
            d1[ptr1] = True
            ptr1 = ptr1.next
        while ptr2:
            d2[ptr2] = True
            ptr2 = ptr2.next
        for i in d1:
            if i in d2:
                return i
        return None