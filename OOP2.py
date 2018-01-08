"""
 2. Create LinkedList Class with methods:
 a) get(i)
 b) put(i)
 c) delete(i)
 d) indexOf(el) - first element = el
 e) size()
 """


class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None 

class LinkedList:
	def __init__(self):
		self.head = None
		
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def getNth(self, index):
		current = self.head 
		count = 0 
		while (current):
			if (count == index):
				return current.data
			count += 1
			current = current.next
		assert(false)
		return 0;

if __name__=='__main__':

	llist = LinkedList()

	# Use push() to construct below list
	# 1->12->1->4->1
	llist.push(1);
	llist.push(4);
	llist.push(1);
	llist.push(12);
	llist.push(1);

	n = 3
	print ("Element at index 3 is :", llist.getNth(n))
