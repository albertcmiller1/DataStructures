class Node:
    def __init__(self, val=None):
        self.val = val 
        self.next = None 


class LinkedList:
    def __itit__(self):
        self.headnode = None 

    
    def traverse(self):
        tempnode = self.headnode
        while tempnode is not None:
            print(tempnode.val)
            tempnode = tempnode.next 


list = LinkedList()
list.headnode = Node("monday")

e2 = Node("tuesday") 
e3 = Node("wedensday") 

# link them together 

list.headnode.next = e2
e2.next = e3

list.traverse()

