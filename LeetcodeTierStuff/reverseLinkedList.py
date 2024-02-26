# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# make a variable called previous which is None
# make a variable called current which is head
# do a while loop for while current is not None
# in the loop, set previous to current
# set a next_node to current.next
# then set current.next to previous
# then set previous to current
# then set current to next_node
# after the loop return previous

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current = head
        previous = None
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
