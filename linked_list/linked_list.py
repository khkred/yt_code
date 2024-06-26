# Basic Node because the value is immutable and the value is declared during initialization
class Node:
    def __init__(self, value, link_node = None):
        self.value = value
        self.link_node = link_node
    
    # Getter for Value
    def get_value(self):
        return self.value
    
    # Getter for Link Node
    def get_link_node(self):
        return self.link_node
    
    # Setter for link node
    def set_link_node(self, next_node):
        self.link_node = next_node


class LinkedList:

    def __init__(self, value = None):
        if value is None:
            self.head_node = None
        else:
            head_node = Node(value)
            self.head_node = head_node

    # Getter for Head Node
    def get_head_node(self):
        return self.head_node
    
    # Insert at Beginning
    def insert_at_beginning(self, value):
        new_node = Node(value)
        current_head_node = self.get_head_node()
        new_node.set_link_node(current_head_node)
        self.head_node = new_node
    
    # Insert at End
    def insert_at_end(self, value):
        current_node = self.get_head_node()
        end_node = Node(value)

        if current_node is None:
            self.head_node = end_node
        else:
            while current_node.get_link_node() is not None:
                current_node = current_node.get_link_node()
            
            current_node.set_link_node(end_node)
    
    # General Format: 5--> 4--> 2 --> None
    def stringify_list(self):
         ll_str = ""
         current_node = self.get_head_node()

         while current_node:
             if current_node is not None:
                 ll_str += str(current_node.get_value()) + " --> "         
             current_node = current_node.get_link_node()
         
         ll_str += "None"
         return ll_str
    
    # a --> b ---> c Results: a --> c
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()

        # If it's Head Node:
        if current_node and current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_link_node()
            current_node = None
        
        else:
            while current_node:
                next_node = current_node.get_link_node()

                if next_node and next_node.get_value() == value_to_remove:
                    current_node.set_link_node(next_node.get_link_node())
                    next_node = None
                else:
                    current_node = next_node
        

    

# Test 1 Linked list with no data
ll_no_value = LinkedList()

print(ll_no_value.stringify_list()) # Prints None

# Test 2 with insert at beginning
ll1 = LinkedList(2)
ll1.insert_at_beginning(4)
ll1.insert_at_beginning(5)    

print(ll1.stringify_list()) # 5 --> 4 --> 2 --> None

# Test 3 with insert at end

ll2 = LinkedList(1)
ll2.insert_at_end(2)
ll2.insert_at_end(3)
ll2.insert_at_end(4)

print(ll2.stringify_list()) # 1 --> 2 --> 3 --> 4 --> None 

# Test 4 with removing the node
ll3 = LinkedList(10) 
ll3.insert_at_end(20)
ll3.insert_at_end(30)
ll3.insert_at_end(40)

ll3.remove_node(30)
print(ll3.stringify_list()) # 10 --> 20 --> 40

