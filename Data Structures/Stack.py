class Stack:
  def __init__(self):
    self.stack = [] # Initialize an empty list to hold stack items
    
  def push(self,item):
    """Add an item to the top of the stack"""
    self.stack.append(item)
    print(f"Pushed {item} onto stack")
    
  def pop(self):
    """Remove and return the top item of the stack"""
    if not self.isEmpty():
      removed_item = self.stack.pop()
      print(f"Popped {removed_item} from the stack") # generally we use 'return' to get the immediate feedback in pop and peek, as a beginner we use print for readability friendliness
    else:
      print("Stack is empty, cannot pop")
      return None
    
  def peek(self):
    """Return top item without removing it (taking a peek!)"""
    if not self.isEmpty():
      top_item = self.stack[-1]
      print(f"Top item is {top_item}")
    else:
      print("Stack is empty, nothing to peek")
      return None
    
  def isEmpty(self):
    """Checking if the stack is empty"""
    return len(self.stack) == 0
  
  def size(self):
    """Return the number of items in the stack"""
    return len(self.stack)
  
  def display(self):
    """Dispaly the entire stack"""
    if self.isEmpty():
      print("Stack is empty!")
    else:
      print("(Stack from top to bottom):")
      for item in reversed(self.stack):
        print(item)