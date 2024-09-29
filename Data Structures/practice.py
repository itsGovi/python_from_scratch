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
        
        
"""Queue's are pretty much the same as Stack, with 5% change FIFO"""


"""BST"""

class Node:
  def __init__(self,key):
    self.right = None
    self.left = None
    self.key = key
    
class BST:
  def __init__(self):
    self.root = None
    
  def insert(self, key):
    return self.__insert(self.root, key)
      
  def _insert(self, current_node, key):
    if current_node is None:
      current_node = Node(key)

    if key < current_node.value:
      self._insert(current_node.left, key)
    
    elif key > current_node.value:
      self._insert(current_node.right, key)
      
  def search(self, key):
    return self._search(self.root, key)
  
  def _search(self, current_node, key):
    if current_node is not key:
      return False
    
    if current_node == key:
      return True
    
    if key < current_node.value:
      self._search(current_node.left, key)
  
    elif key > current_node.value:
      self._search(current_node.right, key)
  
  def inorder_traverse(self,):
    return self._inorder_traverse(self.root)
  
  def _inorder_traverse(self,current_node):
    if current_node:
      self._inorder_traverse(current_node.left)
      
      print(current_node.value, end=' ')
      
      self._inorder_traverse(current_node.right)
      
  def min_value(self):
    return self._min_vaule(self.root)
  
  def _min_value(self,node):
    current = node
    while current.left is not None:
      current = current.left
    return current.value
  
  def max_value(self):
    return self._max_value(self.root)
  
  def _max_value(self, node):
    current = node
    while current.right is not None:
      current = current.right
    return current.value
  
  
"""Graph"""

from collections import deque

class Graph:
  def __init__(self):
    self.graph = {}
    
  def add_vertex(self, vertex):
    if vertex not in self.graph:
      self.graph[vertex] = [] #1
    else:
      print("This vertex already exists, can't add duplicates")
      
  def add_edges(self, vertex1, vertex2):
    if vertex1 and vertex2 in self.graph:
      if vertex1 == vertex2:
        print("Can't add a self loop")
      
    if vertex2 not in self.graph[vertex1]:
      self.graph[vertex1].append(vertex2)
    if vertex1 not in self.graph[vertex2]:
      self.graph[vertex2].append(vertex2)
    else:
      print("Can't finde given two vertices!")
      
  def display(self): #2
    for vertex,edges in self.graph.items(): #3
      print(f"{vertex}: {', '.join(edges)}") #4
    
  def bfs(self,start_vertex):
    vistied = set()
    queue = deque([start_vertex])
    
    while queue: #5
      current = queue.popleft()
      if current not in vistied:
        print(current, end=' ')
        vistied.add(current)
        
      for neighbor in self.graph[start_vertex]:
        if neighbor not in vistied:
          queue.append(neighbor)
          
  def dfs(self, start_vertex):
    visited =set()
    return self._dfs(start_vertex, visited)
  
  def _dfs(self, current, visited):
    if current not in visited:
      print(current, end=' ')      
      visited.add(current)
      
    for neighbor in self.graph[current]:
      if neighbor not in visited:
        self._dfs(neighbor, visited) #6