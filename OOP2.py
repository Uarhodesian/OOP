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
		new_node=node(data)
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

	def get(self,index):
		if index>=self.length():
			print("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	def delete(self,index):
		if index>=self.length():
			print("ERROR: 'Erase' Index out of range!")
			return 
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1

if __name__=='__main__':

	llist = LinkedList()

	# Use push() to construct below list
	# 1->12->1->4->1
	llist.put(1);
	llist.put(4);
	llist.put(1);
	llist.put(12);
	llist.put(1);

