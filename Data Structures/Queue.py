class Queue: # This DS follows FIFO (First in, First Out)
  def __init__(self):
    self.queue = []
    
  def enqueue(self, item):
    """Adding an item to the Queue"""
    self.queue.append(item)
    print(f"{item} has been added to the queue!")
    
  def dequeue(self):
    """Checking if the queue isn't empty and then 'dequeuing'!"""
    if not self.isEmpty():
      dequeued_item = self.queue.pop(0)
      print(f"{dequeued_item} has been removed from the queue!")
    else:
      print(f"There's nothing queued to be removed!")
      
  def peek(self):
    """Taking a peek at the first item in the queue"""
    if not self.isEmpty():
      first_item = self.queue[0]
      print(f"{first_item} is the first item in the queue!")
    else:
      print("There's nothing to peek as nothing is queued")
    
  def size(self):
    """Getting the total values in the queue""" 
    return len(self.queue)
  
  def isEmpty(self):
    return len(self.queue)==0
  
  def display(self):
    """Getting all the items the queue displayed"""
    if self.isEmpty():
      print("The queue has none items to display! Add and then run the code again!")
    else:
      print("(Queue from front to back):")
      for item in self.queue:
        print(item)