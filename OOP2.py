"""
 2. Create LinkedList Class with methods:
 a) get(i)
 b) put(i)
 c) delete(i)
 d) indexOf(el) - first element = el
 e) size()
 """
class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=node()


	def put(self,data):
		new_node=node()
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	def size(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 


if __name__=='__main__':

	llist = LinkedList()

	# Use push() to construct below list
	# 1->12->1->4->1
	llist.put(1)
	llist.put(4)
	llist.put(1)
	llist.put(12)
	llist.put(1)

