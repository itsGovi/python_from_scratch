"""LINKEDLIST"""
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
    
    
class LinkedList:
  def __init__(self,data):
    self.head = None
    
  def add(self,data):
    new_node = Node(data) #1
    
    if self.head is None:
      self.head = new_node  #2
    else:
      current = self.head
      while current.next is not None:
        current = self.data  #4
      current.next = new_node  #5
      
  def remove(self,data):
    if self.head is None:
      print("There's nothing remove!")
      
    if self.head == data:
      self.head = self.head.next
      return  #6
      
    current = self.head
    while current is not None:
      if current.next.data == data:  #7
        current.next = current.next.next
        return
      current = self.next
    print(f"Node with data {data} is not found")
    
  def traverse(self):
    current = self.head
    if current is None:
      print("The list is empty!")
    while current.next is not None:
      print(current.data, end="-> ")  #8
    return current.data
  
  
"""STACK"""
class Stack:
  def __init__(self):
    self.stack = []
    
  def push(self,item):
    self.stack.append(item)
    print(f"The item {item} has been added to the stack")
    
  def pop(self,item):
    if self.isEmpty():
      print("The stack is empty!")
      return None  #2
    else:
      pop_item = self.stack.pop[-1]
      print(f"The item {pop_item} has been removed")
      
  def peek(self):
    if self.isEmpty():
      print("There's nothing to peek (stack is empty)!")
    else:
      top_item = self.stack[-1]
      print(f"The 1st item on stack is {top_item}")
      
  def isEmpty(self):
    return len(self.stack) == 0
  
  def size(self):
    return len(self.stack)
  
  def display(self):
    if self.isEmpty():
      print("There's nothing to display!")
    while self.stack is not None:
      for item in reversed(self.stack):  #1
        print(item)
        
        
"""Queue"""

class