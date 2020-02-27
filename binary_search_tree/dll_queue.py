import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0 # its makes it easy to always know how many items we have in our queue/ds
        # Why is our DLL a good choice to store our elements?
            # it's the underlying data structure that will store our elements in our queue and will make it easier for us to facilitate the FIFO ordering that we're trying to achieve
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)


    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None
            
    def len(self):
        return self.size


# Notes

# What's the opposite of FIFO ordering? WHat data structure(s) exhibit ordering?

# What data structure(s) would you use to implement a queue?

# When is FIFO ordering useful? WHen is it not? 
    #                     

# Pros
    # queues are simple and intuitive to use and implement
    # they can be used to serialize data coming in from multiple sources

# Cons
    # are not general-purpose at all in and of themselves