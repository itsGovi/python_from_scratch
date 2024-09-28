class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        new_node = Node(data) #Assigning self.head to self.data would only copy the reference, not the actual data.

        if self.head is None: #checking if head node is not there -> marking it as no node yet added
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node  #This loop is essentially asking: "Am I at the last node yet?" If not, it keeps moving to the next node.

    def remove(self,data):
        if self.head is None:
            print("List is empty, nothing to remove")
            return # there' nothing to return
        
        if self.head.data == data:
            self.head == self.head.next #if data and head have same 'data' then make head == data
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == data: #So this line is asking: "Does the next node contain the data we are looking for?" If yes, we are ready to remove it.
                current.next = current.next.next #In other words, we are making the current node point directly to the node after the one we’re removing, effectively "cutting out" the node that matched the data.
                return
            current = current.next #If the next node does not contain the data we’re looking for, we move on to the next node by setting current = current.next.
        
        print(f"Node with data {data} is not found")

    def traverse(self):
        current = self.head
        if current is None:
            print("List is empty!")
        else:
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next # move on to the next node
            print("None") # To indicate end of the list