# linked lists are made of nodes
# a node is a container for some data
# a linked list contains many nodes
# 0    1    2    3 are the node positioons
# a -> b -> c -> d
# a.next = b, b.next = c, c.next = d, d.next = None (null)
# a is head, d is....so linkedlist.head = a and linkedlist.tail = d....head.next = b
# a linked list is linear and not stored at contiguous memory locations, arrays are stored at contiguous memory locations
# so a linked list is implemented on the heap memory rather than the stack memory
# if I wanna insert q into the linked list at position 2, I'd create a new node in memory
# I would do this I would adjust b.next = q, and then q.next = c so:
# 0   1   2   3   4 are the new positions
# a - b - q - c - d are how the nodes link and correspond
# unlike in an array I wouldn't have to insert at O(n) time but at O(1) time
# core linked list traversal algorithim:
# a current reference to look at the current node of the iteration
# look at current.next and set current to equal current.next
# once current.next = null, that is the end of the linked list and the algorithim can stop
