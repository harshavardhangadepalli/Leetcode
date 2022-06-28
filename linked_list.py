class ListNode:
	def __init__(self,val=None,next=None):
		self.val = val
		self.next = next
class LinkedList:
	def __init__(self,head=None):
		self.head = head
	def getValues(self):
		values_lst = list()
		while self.head.next!=None:
			values_lst.append(self.head.val)
			self.head = self.head.next
		if(self.head.val!=None):
			values_lst.append(self.head.val)
			self.head = self.head.next
		return(values_lst)

class Solution:
	def mergeTwoLists(self,l1,l2):
		if not l1 and not l2:
			return None
		elif not l1:
			return l2
		elif not l2:
			return l1

		ptr1 = l1.head
		ptr2 = l2.head
		l_new = LinkedList()
		l_new.head = None
		ptr3 = l_new.head
		while ptr1!=None and ptr2!=None:
			if ptr1.val <= ptr2.val:
				if(l_new.head==None):
					l_new.head = ptr1
					ptr3 = ptr1
					ptr1 = ptr1.next
				else:
					ptr3.next = ptr1
					ptr3 = ptr3.next
					ptr1 = ptr1.next
			else:
				if(l_new.head==None):
					l_new.head = ptr2
					ptr3 = ptr2
					ptr2 = ptr2.next
				else:
					ptr3.next = ptr2
					ptr3 = ptr3.next
					ptr2 = ptr2.next
		#here we check if it is broken because of ptr1 or ptr2
		if ptr1==None:
			while ptr2!=None:
				ptr3.next = ptr2
				ptr3 = ptr3.next
				ptr2 = ptr2.next
		elif ptr2==None:
			while ptr1!=None:
				ptr3.next = ptr1
				ptr3 = ptr3.next
				ptr1 = ptr1.next
		else:
			l_new.next = None
		return(l_new.head)

if __name__ == "__main__":
	l1 = LinkedList()
	first = ListNode(val=2)
	second = ListNode(val=5)
	third = ListNode(val=7)
	l1.head = first
	first.next = second
	second.next = third
	l2 = LinkedList()
	fourth = ListNode(val=1)
	fifth = ListNode(val=8)
	sixth = ListNode(val=10)
	l2.head = fourth
	fourth.next = fifth
	fifth.next = sixth

	sol = Solution()
	sol.mergeTwoLists(l1,l2)