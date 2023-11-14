# define a Node class to represent individual nodes
class Node:
    def __init__(self, data=None):
        # each node contains data and reference to the next node
        self.data = data
        self.next_node = Node

# Define a LinkedList class to manage the linked list


class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with a head node
        self.head = None

    def is_empty(self):
        # Add a new node with the given data
        return self.head is None

    def append(self, data):
        # Add a new node with the given data to the end of the linked list
        new_node = Node(data)
        if self.is_empty():

            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
