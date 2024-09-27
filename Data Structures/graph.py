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
    else:
      print(f"{vertex} already exists in the graph!")
  
  def add_edge(self, vertex1, vertex2):
    """Add an undirected edge between vertex1 and vertex2"""
    if vertex1 in self.graph and vertex2 in self.graph:
     # Ensuring no self-loop is added
     if vertex1 == vertex2:
       print("Cannot add a self-loop!")
       return
     
     # Add edge only if it doesn't already exist
     if vertex2 not in self.graph[vertex1]:
       self.graph[vertex1].append(vertex2)
       
     if vertex1 not in self.graph[vertex2]:
        self.graph[vertex2].append(vertex1)
     else:
       print("One or both vertices do not exist!")
      
  def display(self):
    """Display the graph"""
    for vertex,edges in self.graph.items():
      print(f"{vertex}: {', '.join(edges)}")
      
  def bfs(self, start_vertex):
    """Breadth-First Search (BFS) traversal starting from start_vertex."""
    visited = set()
    queue = deque([start_vertex])
    
    while queue:
      current_vertex = queue.popleft() # Pop the 1st element from the queue
      if current_vertex not in visited:
        print(current_vertex, end=' ') # Process(print) the vertex
        visited.add(current_vertex) # Marking the vertex as visited
        
        # Adding all neighbors to the queue
        for neighbor in self.graph[current_vertex]:
          if neighbor not in queue:
            queue.append(neighbor)
            
  def dfs(self, start_vertex):
    """Depth-First Search (DFS) traversal starting from start_vertex."""
    visited = set()
    self._dfs_recursive(start_vertex, visited)
    
  def _dfs_recursive(self, vertex, visited):
    """Helper Function"""
    if vertex not in visited:
      print(vertex, end=' ')
      visited.add(vertex)
      
      # Recursively visit all the unvisited neighbors
      for neighbor in self.graph[vertex]:
        if neighbor not in visited:
          self._dfs_recursive(neighbor, visited) 