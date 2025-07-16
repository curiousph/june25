# This program checks if a linked list has a cycle using Floyd's Tortoise and Hare algorithm.

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    """
    Returns True if the linked list has a cycle, False otherwise.
    Uses Floyd's Tortoise and Hare algorithm for cycle detection.
    """
    slow = head  # Moves one step at a time
    fast = head  # Moves two steps at a time

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # Cycle detected

    return False  # No cycle

# Example usage and test cases
if __name__ == "__main__":
    # Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 2 ...
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle

    print("List with cycle:", has_cycle(node1))  # Should print True

    # Create a linked list without a cycle: 1 -> 2 -> 3 -> 4
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None

    print("List without cycle:", has_cycle(node1))  # Should print False