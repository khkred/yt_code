class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    def append(self, value):
        current_node = self.head
        add_node = Node(value)
        if not current_node:
            self.head = add_node
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = add_node
        
    
    def print_list(self):
        current_node = self.head
        if not current_node:
             print("Empty List")
        
        else:
            while current_node:
                print(current_node.data, end=" ")
                current_node = current_node.next 
        print()
    
    def rev_list(self):
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        self.head = prev
        


linkedList = LinkedList()

linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.append(5)

linkedList.print_list()

linkedList.rev_list()
linkedList.print_list()
