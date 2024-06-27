class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, new_data):
		new_node = Node(new_data)

		# If head is Null
		if not self.head:
			self.head = new_node
		else:
			last = self.head

			while last.next:
				last = last.next

			last.next = new_node


	def print_list(self):
		temp = self.head

		if not temp:
			print("Empty LinkedList")
		else:
			while temp:
				print(temp.data, end = " ")
				temp = temp.next
		print()


	def swap(self, x, y):

		# If x and y are same

		if x == y:
			return

		prevX = None

		currX = self.head

		while currX and currX.data != x:
			prevX = currX
			currX = currX.next


		prevY = None

		currY = self.head

		while currY and currY.data != y:
			prevY = currY
			currY = currY.next


		# Make sure that neither CurrX or CurrY are null

		if not currX or not currY:
			return

		if not prevX:
			self.head = currY
		else:
			prevX.next = currY


		if not prevY:
			self.head = currX
		else:
			prevY.next = currX


		temp = currX.next

		currX.next = currY.next

		currY.next = temp



ll_list = LinkedList()

ll_list.append(5)
ll_list.append(10)
ll_list.append(15)
ll_list.append(34)
ll_list.append(56)

ll_list.print_list()

ll_list.swap(5,34)

ll_list.print_list()

















