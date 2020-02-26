from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # 
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList() # 
        self.storage = dict() # or {} -- same thing

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Access value from given key
        # Move key/value pair to the MRU end of list
        # Return value or None if None
        if key in self.storage[key]:
            node = self.storage[key] # need to move to tail because it was MRU
            self.order.move_to_end(node)
            return node.value[1] # accessing the value in the key/value pair
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Put/Set:
            # Move to head of list
            # Add hash table entry (MRU)
            # If over-full
                # simply delete the tail entry from the DLL and the has table
        # Create node if key not found
        # Move node to front (head) if key not found

        if key in self.storage:
            node = self.storage[key] # grabbing the full node
            node.value = (key, value) # overwritting the value but keeping the k/v pair
            self.order.move_to_end(node) # node is a pointer here + MRU
            return # nothing else to do, exit the function
        # If full, remove last node from LL and the hash map / dictionary
        if self.size == self.limit: # check if its full
            del self.storage[self.order.head.value[0]] # remove LRU from dict 
            self.order.remove_from_head() # remove from LL
            self.size -= 1  # 
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1


# In class notes--
        # If the cache is empty
            # Add to linked list with the key and value
            # Add the key and value to the dictionary
            # increment the size
        # If cache is not empty
            # check if key is in dictionary
                # if it is
                    # overwrite the value
                    # move it to the MRU end of list
                # if it is not
                    # check if its full
                        # if cache is not full
                            # same as if cache is empty
                        # if cache is full
                            # remove the LRU from the dictionary and LL
                            # reduce the size
                            # same as if cache is empty

    # Re- organizing top pseudo

        # check if key is in dictionary
            # if it is
                # overwrite the value
                # move it to the MRU end of list
            # if it is not
                    # check if its full
                        # if cache is full
                            # remove the LRU from the dictionary and LL
                            # reduce the size
            # Add to linked list with the key and value
            # Add the key and value to the dictionary
            # increment the size
        

