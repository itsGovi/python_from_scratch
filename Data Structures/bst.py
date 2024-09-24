"""RECURSIVE: relating to or involving a program or routine of which a part requires the application of the whole, 
so that its explicit interpretation requires in general many successive executions."""

class Node:
  def __init__(self):
    self.right = None # right child
    self.left = None  # left child
    self.value = key  # Node's value
    
class BinarySearchTree:
  def __init__(self):
    self.root = None # The first node -> root of the tree
    
  def insert(self, key):
    if self.root is None:
      self.root = Node(key)
    else:
      self._insert(self.root, key)
      
  def _insert(self, current_node, key):
    if key < current_node.value:
      # Insert in the left subtree
      if current_node.left is None:
        current_node.left = Node(key)
      else:
        self._insert(self.current_node.left, key)
        #calling its own function for searching the lowest position to place it!
    elif key > current_node.value:
      if current_node.right is None:
        current_node.right = Node(key)
      else:
        self._insert(current_node.right, key)
        #calling its own function for searching the highest position to place it!
  
  def search(self, key):
    """Search for a node with the given key"""
    return self._search(self.root, key)
  
  def _search(self, current_node, key):
    """Helper method to search for a key in the tree"""
    if current_node is None:
      return False # key not found
    
    if current_node.value == key:
      return True # key found
    
    if key < current_node.value:
      return self._search(current_node.left, key)
    else:
      return self._search(current_node.right, key)
    
  def inorder_traverse(self):
    """Traverse the tree in-order (Left, Root, Right)"""
    self._inorder_traverse(self.root)
    
  def _inorder_traverse(self, current_node):
    if current_node:
      # Traverse left subtree
      self._inorder_traverse(current_node.left)
      # print the node
      print(current_node.value, end=' ')
      # Traverse right subtree
      self._inorder_traverse(current_node.right)
      
  def min_value(self):
    return self._min_value_node(self.root)
  
  def _min_value_node(self, node):
    current = node
    while current.left is not None:
      current = current.left
    return current.value
    
  def max_value(self):
    return self._max_value_node(self.root)
  
  def _max_value_node(self, node):
    current = node
    while current.right is not None:
      current = current.right
    return current.value