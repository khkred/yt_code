class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head

            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp, end = " --> ")
            temp = temp.next
            
        print()

    def pop_at_nth_place(self, n):

        #Another node that is n places behind our current node

        current_node = self.head
        tmp_node = None
        count = 0

        while current_node:
            current_node = current_node.next
            count += 1

            if count >= n:
                if tmp_node is None:
                    tmp_node = self.head
                else:
                    tmp_node = tmp_node.next
        
        return tmp_node.data
    
    # Pop Middle of the list
    # Find cyclic LinkedList
    # Pop at any place


ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.append(7)

print(ll.pop_at_nth_place(2))



        





