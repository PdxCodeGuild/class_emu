class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, key):
        #Make a temp to store head
        temp = self.head
        
        #Check to see if the data to be deleted is head
        if(temp is not None): #Make sure list isn't empty. Head will = Null if it is
            if (temp.data == key): #if temp is equal to the key
                self.head = temp.next #Make head = the node after the one to be deleted
                temp = None #zero out temp since it is now the key to be deleted
                return
        
        #Because the data to be deleted is NOT head, loop and find it

        while(temp is not None): #loop until you hit NULL
            if (temp.data == key):
                break  #If you find the key, break from the loop
            prev = temp #Make a copy of temp so it can keep track of what temp was since temp is about to "move"
            temp = temp.next #move temp to the next node

        if(temp == None):  #if key was not present in the list
            return

            #unlink the node from the list
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


newList = LinkedList()
newList.push(1)
newList.push(2)
newList.push(3)
newList.push(4)
newList.push(5)
print(f"Before:")
newList.printList()
print(f"After:")
newList.delete(3)
newList.delete(5)
newList.printList()

