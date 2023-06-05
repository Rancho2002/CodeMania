# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
# @param A : head node of linked list
# @return the head node in the linked list
    def deleteDuplicates(self, A):
        current = A
        nxt = current.next
        while current:
                if nxt.val == current.val:
                    nxt = nxt.next
                
                else:
                    current.next = nxt
                    current = nxt
                    nxt = nxt.next
                    current = current.next
        return A
a=Solution()
A=[]