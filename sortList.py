# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):

        def getMid(header):
            slow = header
            fast = header.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(left, right):
            # dummy exists just for entering the first element
            # dummy used to remember head
            dummy = ListNode()
            # tail used to keep track of end
            tail = dummy
            # while there are remaining elements of left and right
            while left and right:
                # if the left is greater, assign that to tail.next
                # then move left by one step
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                # if the right is greater, then do the same for right
                # right+=1
                else:
                    tail.next = right
                    right = right.next
                # then tail+=1
                tail = tail.next
            # if all the elements are done in either array,
            # assign remaining to tail.next as it is ( already sorted )
            tail.next = right if right else left
            # returning first node of dummy
            return dummy.next

        # checking if the head is None or head.next is None
        if not head or not head.next:
            return head

        # for each linked list, get the middle
        mid = getMid(head)
        # mid will mark the middle of the list
        # now we need to split the list into head to mid and mid to end
        # tmp will be the first element of the right part
        # mid will be the last element of the left
        # mid should point to nothing (end of that part)
        tmp = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(tmp)

        return merge(left, right)
