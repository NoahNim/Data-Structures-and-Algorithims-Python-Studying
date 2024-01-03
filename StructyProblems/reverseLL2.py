class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
    previous = None  # points to previous node
    current = head
    while current is not None:
        next = current.next  # saves the value of the next node
        current.next = previous  # sets the next to be previous
        previous = current  # makes the previous node become the current node of the iteration
        current = next  # moves the current node to the node that was originally next
    return previous
