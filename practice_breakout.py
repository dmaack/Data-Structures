def find_middle(head):
    end = head
    middle = head
    length = 0

    while end.next != None:
        length += 1
        if length % 2 == 0:
            middle = middle.next
        end = end.next

    return middle.value

class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
    def add(self, value):
        self.next = Node(value)


node = Node(5)
node.add(6)
node.next.add(8)
node.next.next.add(10)

print(node)


