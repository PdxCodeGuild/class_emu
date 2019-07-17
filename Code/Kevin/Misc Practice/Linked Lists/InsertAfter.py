class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def insertafter(self, previous_node, data): #5 step process. 
        if previous_node is None:     # Can't insert if there is no previous node. Can probably add a push method here
            print("Previous node is non-existent.")
            return
        
        new_node = Node(data)   # Always start off with making a new node and placing data in it.
        new_node.next = previous_node.next
        previous_node.next = new_node
 
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next 


myLinkedList = LinkedList()
myLinkedList.push("Hello ")
myLinkedList.insertafter(myLinkedList.head, "world!")

myLinkedList.printList()

