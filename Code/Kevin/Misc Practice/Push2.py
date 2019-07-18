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

    def insert(self, previous_node, data):
        
        #check and see if previous node exists        
        if previous_node is None:
            print("The previous node is NULL.")
            return
        
        #create new node and put data in it
        new_node = Node(data)

        #make new node's next = previous_node's next
        new_node.next = previous_node.next

        #make previous node's next = new_node
        previous_node.next = new_node

    def append(self, new_data):
        
        #create a new node and put data in it
        new_node = Node(new_data)

        #check and see if head is = to the wall (NULL)
        if self.head is None:
            new_node.next = self.head  #if head is NULL do a push without creating a new node
            self.head = new_node

        else:   #if head isn't the wall, make temp head....Remember, head is JUST A POINTER! NOT DATA
            temp = self.head
            while(temp.next):   #Make temp next until next is the wall. 
                temp = temp.next
            temp.next = new_node #Make temp's next point at the new node. The new node auto points to the wall
        
