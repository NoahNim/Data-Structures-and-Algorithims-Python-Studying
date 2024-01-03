# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
    current = head
    current_index = 0
    while current is not None:
        if current_index == index:
            return current.val
        current = current.next
        current_index += 1
    return None
