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
    - if value is less than node
        - go left and repeat
        - if no left child -- return none
    - if value is greater or equal to node
        - go right and repeat
        - if no right child -- return none

Get Max --
    - While you can go right go right
    - If no right child, return this value, otherwise go right



'''