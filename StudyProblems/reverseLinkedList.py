def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #    stack = deque()
    # current = head
    # new_linked_list = ListNode()

    # while current:
    #     stack.appendleft(current.val)
    #     current = current.next
    # current = new_linked_list
    # for node in stack:
    #     current.next = ListNode(node)
    #     current = current.next
    # return new_linked_list.next

    current = head
    previous = None

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous
