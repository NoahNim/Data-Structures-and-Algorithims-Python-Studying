class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# make a pointer for position, current, next, and previous
# loop through linked list, increment positioon by 1 each time
# in the loop, have current also have a pointer called old_current
# if position is the given index....
# set previous.next to value, set current to value, set current.next to old_current
# set current.next.next to next


def insert_node(head, value, index):
    position = 0
    current = head
    previous = None
    next = current.next
    if index == 0:
        old_current = current
        head = Node(value)
        head.next = old_current
        old_current.next = next
        return head
    while current is not None:
        old_current = current
        next = current.next
        if position is index:
            current = Node(value)
            previous.next = current
            old_current.next = next
            current.next = old_current
            return head
        previous = current
        current = current.next
        position += 1
    if current is None:
        current = Node(value)
        previous.next = current
        return head
