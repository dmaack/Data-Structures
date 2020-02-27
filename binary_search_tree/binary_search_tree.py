import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree: # more like SLL for the stack prob
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # print(f'value:', self.value, f'left:', self.left, f'right:', self.right)

    # Insert the given value into the tree
    def insert(self, value):
        root = self
        new_node = BinarySearchTree(value)

        if value < root.value:
            if root.left is None:
                root.left = new_node
            else:
                root.left.insert(value)
        elif value >= root.value:
            if root.right is None:
                root.right = new_node
            else:
                root.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if self.value == target:
            return True
        elif self.value < target: 
            if self.right is None:
                return None
            else:
                return self.right.contains(target)
        elif self.value >= target:
            if self.left is None:
                return None
            else:
                return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        root = self

        if root.right is None:
            return root.value
        else:
            return self.right.get_max()
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass # queue?

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
