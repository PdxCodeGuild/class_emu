class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data): # Pushing the data to the top of the stack.      Today?->You->Are->How->World!->Hello

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        full_word = ""
        while(temp):
            full_word += temp.data
            temp = temp.next
        print(f"Full Word: {full_word}")

mylinkedList = LinkedList()

mylinkedList.push("Hello ")
mylinkedList.push("world ")

mylinkedList.printlist()





