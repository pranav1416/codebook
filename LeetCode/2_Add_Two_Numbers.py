# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		ctr = 1
		val_1 = 0
		val_2 = 0
		res = 0
		flag = 0
		while(flag!=1):
			if(l1.next == None and l2.next == None):
				flag = 1
			if(l1.val!= None):
				val_1 += l1.val * ctr
				l1 = l1.next
			if(l2.val!= None):
				val_2 += l2.val * ctr
				l2 = l2.next
			ctr *=10
		res = val_1 + val_2
		res = list(map(int,str(res)))
		node = ListNode(-1)
		for i in range(0,len(res)):
			if(node.val == -1):
				node.val = res[i]
			else:
				head_node = ListNode(res[i],node)
				node = head_node
		while(True):
			print(node.val)
			if(node.next==None):
				break
			node = node.next

if __name__ == "__main__":
	test = Solution()
	x1 = ListNode(1)
	x2 = ListNode(2,x1)
	x3_head = ListNode(3,x2)

	y1 = ListNode(7)
	y2 = ListNode(8,y1)
	y3_head = ListNode(9,y2)

	test.addTwoNumbers(x3_head, y3_head)