class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None: # Check to see if head is pointing to null. If so, add new_data to the front of the queue
            self.head = new_node
            return
    
        last = self.head
        while(last.next): #Keep moving while you have a next node and don't point to null
            last = last.next
        
        last.next = new_node #Dunno why, but this changes the last node to point to the new node....Instead of changing the new node (last), I just made.

    def PrintList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
myList = LinkedList()

myList.append(10)
myList.append(20)
myList.append(30)

myList.PrintList()
