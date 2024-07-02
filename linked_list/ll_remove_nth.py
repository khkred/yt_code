class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases such as removing the first node
        dummy = ListNode(0)
        
        dummy.next = head
        slower_node = dummy
        faster_node = dummy

        # Move faster_node n+1 steps ahead
        for _ in range(n + 1):
            faster_node = faster_node.next

        # Move both nodes until faster_node reaches the end
        while faster_node:
            faster_node = faster_node.next
            slower_node = slower_node.next

        # Remove the nth node from the end
        slower_node.next = slower_node.next.next

        return dummy.next
