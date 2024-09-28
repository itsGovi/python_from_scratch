from graph import Graph

if __name__ == "__main__":
    # Create a graph instance
    g = Graph()

    # Add vertices
    vertices = ["A", "B", "C", "D", "E"]
    for vertex in vertices:
        g.add_vertex(vertex)

    # Add edges (undirected)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")

    # Display the graph
    print("Graph:")
    g.display()

    # Perform BFS
    print("\nBFS Traversal starting from vertex A:")
    g.bfs("A")

    # Perform DFS
    print("\n\nDFS Traversal starting from vertex A:")
    g.dfs("A")
    
""" 
How the graph looks as drawing:
   A
  / \
 B   C
  \ / 
   D
    \
     E
"""