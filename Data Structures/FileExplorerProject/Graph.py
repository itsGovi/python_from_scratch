import matplotlib.pyplot as plt
import networkx as nx

class Graph:
  """Represents symbolic links between files and directories as an undirected graph"""
  def __init__(self):
    self.graph = {}
    
  def add_link(self, file1, file2):
    """Adds a symbolic link between two files or directories"""
    if file1 not in self.graph:
      self.graph[file1] = []
    if file2 not in self.graph:
      self.graph[file2] = []
    self.graph[file1].append(file2)
    self.graph[file2].append(file1)
    
  def display_links(self):
    """Displays all the symbolic links"""
    for key, value in self.graph.items():
      print(f"{key}: {', '.join(value)}")
      
  def visualize_graph(self):
    """Create a visual representation of the file graph"""
    G = nx.Graph()
    for file1, connections in self.graph.items():
      for file2 in connections:
        G.add_edge(file1,file2)
        
    plt.figure(figsize=(8,6))
    nx.draw(G, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
    plt.show()