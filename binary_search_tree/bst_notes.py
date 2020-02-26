'''

Binary Search Trees

    What are they?


Binary -- usually O(logn)
    - worse case? it would be a linked list O(n)
    - best case usage is if you have to do a lot of look-ups / comparisons with data that can be ordered 
         - ex -- list of parts for cars, which there are a lot, and you want to lookup if you have a part, if parts were ordered alphabetically, it would be a fast look up



Pseudocode for functions:


Insert --
    - compare root node
        - if lesser go to left child
        - if greater go to right child
        - if no child, insert
        - else try again starting from the child on the appropriate side

Contains / Find --
    - Look at root
        - if its root then return
    - if value is less than node
        - go left and repear
        - if no left child -- return none
    - if value is greater or equal to node
        - go right and repeat
        - if no right child -- return none

Get Max --
    - Go right until no more right



'''