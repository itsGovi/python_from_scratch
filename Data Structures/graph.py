from collections import deque

class Graph:
  def __init__(self):
    """The reason why graph uses DICT rather than LIST which
    Queue's, LinkedList's, Stack and BST's use?
    REASON:
      graph = {
      'A': ['B', 'C'],
      'B': ['A', 'D'],
      'C': ['A'],
      'D': ['B']
      }
    In this representation, the key 'A' is associated with a list containing its adjacent nodes 'B' and 'C'.

    Advantages of using dictionaries for graphs:

    Efficient lookup: Dictionaries provide efficient lookup of adjacent nodes using the node's key.
    Flexibility: Dictionaries can easily handle graphs with different types of nodes and edges.
    Dynamic updates: Adding or removing nodes and edges can be done efficiently in dictionaries.  
  """
    self.graph = {}
    
  def add_vertex(self, vertex):
    if vertex not in self.graph:
      self.graph[vertex] = [] # Initialize an empty list for edges
  
  def add_edge(self, vertex1, vertex2):
    """Add an undirected edge between vertex1 and vertex2"""
    if vertex1 in self.graph and vertex2 in self.graph:
      