class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
    
class LinkedList:
  def __init__(self,data):
    self.head = None
    
  def add(self,data):
    new_node = Node(data) 1
    
    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next is not None:
        current = self.data
      current.next = new_node
      
  def remove(self,data):
    if self.head is None:
      print("There's nothing remove!")
      
    if self.head == data:
      self.head = self.head.next
      return
      
    current = self.head
    while current is not None:
      if current.next.data == data:
        current.next = current.next.next
        return
      current = self.next
    print(f"Node with data {data} is not found")
    
  def traverse(self):
    current = self.head
    if current is None:
      print("The list is empty!")
    while current.next is not None:
      print(current.data, end="-> ")
    return current.data