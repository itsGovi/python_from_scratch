class NavigationStack:
  """Handles 'BACK' navigation using a stack (LIFO)"""
  def __init__(self):
    self.stack = []
    
  def push(self,path):
    """Pushes the current path onto the stack"""
    self.stack.append(path)
    
  def pop(self):
    """Pops the last path from the stack"""
    return self.stack.pop() if self.stack else None
  
  class NavigationQueue:
    """Handles 'FORWARD' navigation using queue (FIFO)"""
    def __init__(self):
      self.queue = []
      
    def enqueue(self, path):
      """Enqueues the current path to the forward queue"""
      self.queue.append(path)
      
    def dequeue(self):
      """Dequeues the next path from the forward queue"""
      return self.queue.pop(0) if self.queue else None