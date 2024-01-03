class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# return linked list values in a list


def linked_list_values(head):
    list_vals = []
    current = head
    while current is not None:
        list_vals.append(current.val)
        current = current.next
    return list_vals
