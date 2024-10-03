from file_structure import FileTree
from stack_queue import NavigationStack, NavigationQueue
from graph import Graph

class FileExplorer:
  """Main file explorer class that manages all operations"""
  def __init__(self):
    self.file_tree = FileTree() # Directory and file management
    self.back_stack = NavigationStack() # "Back" navigation history
    self.forward_queue = NavigationQueue() # "Forward" navigation history
    self.links = Graph() # Symbolic links between files and directories
    self.current_path = [] # current path as a list of directories
    
  def add_file_or_directory(self):
    """Adds a file or directory at the current path"""
    name = input("Enter the name of the file or directory: ")
    is_directory = input("Is it a directory? (yes/no): ").lower() == 'yes'
    self.file_tree.add_file(self.current_path, name, is_directory)
    
  def delete_file_or_directory(self):
    """Deletes a file or directory from the current path"""
    name = input("Enter the name of the file or directory to delete: ")
    self.file_tree.delete_file(self.current_path, name)
    
  def search_file(self):
    """Searches for a file or directory by name"""
    name = input("Enter the name of the file or directory to search: ")
    self.file_tree.search_file(name)
    
  def navigation_back(self):
    """Navigation back in the directory structure"""
    if self.current_path:
      self.forward_queue.queue(self.current_path.copy())
      last_dir = self.current_path.pop()
      self.back_stack.push(self.current_path.copy())
      print(f"Moved forward to {'/'.join(self.current_path)}")
    else:
      print("Already at root directory")
      
  def navigate_forward(self):
    """Navigates forward in the directory structure"""
    if self.forward_queue.queue:
      self.back_stack.push(self.current_path.copy())
      self.current_path = self.forward_queue.dequeue()
      print(f"Moved forward to {'/'.join(self.current_path)}")
    else:
      ("No forward history available")
      