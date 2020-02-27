'''

Binary Search Trees

    What are they?


Binary -- usually O(logn)
    - worse case? it would be a linked list O(n)
    - best case usage is if you have to do a lot of look-ups / comparisons with data that can be ordered 
         - ex -- list of parts for cars, which there are a lot, and you want to lookup if you have a part, if parts were ordered alphabetically, it would be a fast look up



Pseudocode for functions:


Insert --
    -if there is no node at root, insert this as root -- base case!
    Otherwise:
    - compare value to root node
        - if value lesser go (look) to left child
            - if no node, make new one with this value
        - if value greater or equal go to right child
            - if no node, make new one with this value
        - if no child, insert
        - else try again starting from the child on the appropriate side


Contains / Find -- on average O(logn) -- everytime you go one direction, you cut off half of the results | worst case O(n) because it could look like something like a LL
    - If no node at root 
        -return false
    - Compare value to root
        - if its root then return
    - if target is less than node
        - go left and repeat
        - if no left child -- return none
    - if target is greater or equal to node
        - go right and repeat
        - if no right child -- return none

Get Max --
    - While you can go right go right
    - If no right child, return this value, otherwise go right



Day 2 lecture notes:

    re-psuedo coding for solutions:

    Insert:
        - if value is less than node.value, look left
            - check if something is there
                -if something is there 
                    - recurse left
                - else if not
                    - insert left
        - otherwise if value is greater or equal to than node.value, look right
            - check if something is there
                - if something is there
                    - recurse right
                - else if not
                    - insert right

        INSERT CODE SOLUTION:

        if value < self.value
            if self.left:
                self.insert(value)
            else:
                self.left = BinarySearchTree(value)
        if value >= self.value:
            if self.right:
                self.insert(value)
            else:
                self.left = BinarySearchTree(value)        

- what is the base case for the insert function?
    - it creates a new node
    - you cant call the insert function unless you have created a node
    

    Conatins / Find:
        -

    CONTAINS CODE SOLUTION:

    if self.value == target:
        return True
    if self.value < target:
        if self.left:
            return self.left.contains(target)
        else:
            return False
    if self.value >= target:
        if self.right:
            return self.right.contains(target)
        else:
            return False 


- what is the clue that we need to write a base case?
    - we have a target and we do that by returning information
        - where does function exit when you return true? 
            - 


    GET MAX CODE SOLUTION:

    if not self.right:
        return self.value
    else:
        return self.right.get_max()
'''