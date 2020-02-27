import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1 # need to increment the size by one
        self.storage.add_to_head(value) # if no head, then head and tail are the new node value / else (if there is at least one node, this head is the new node, this head next is the old begining)

    def pop(self):
        if self.size == 0: # if the list is empty, return none
            return 
        else:
            value = self.storage.remove_from_head() # remove the value that was last added which will be the head
            self.size -= 1 # decrese the size by 1
        return value

        


    def len(self):
        return self.storage.__len__()
