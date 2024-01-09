# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# have a pointer for curent and previous and next
# if current.val is the target, make current = next, current.next = next.next, and previous.next = current

def remove_node(head, target_val):
    current = head
    next = current.next
    previous = None

    if head.val == target_val:
        head = head.next
        return head

    while current is not None:
        next = current.next
        if current.val == target_val and previous is not None:
            current = next
            previous.next = current
            break
        previous = current
        current = current.next
    return head
