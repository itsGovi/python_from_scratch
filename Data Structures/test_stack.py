from stack import Stack

if __name__ == "__main":
  my_stack = Stack()
  
  # Push items to stack
  my_stack.push('phewww')
  my_stack.push('kaboom')
  my_stack.push('di-shum')
  my_stack.push('pow')
  my_stack.push('bang')
  my_stack.push('ka-ching')
  
  # Display stack
  print("\nCurrent Stack:")
  my_stack.display()
  
  # Peek at the top item
  print("\nPeeking at the top item:")
  my_stack.peek()
  
  # Pop the top item
  print("\nPop the top item:")
  my_stack.pop()
  
  # Displaying stack after pop
  print("\nStack after pop:")
  my_stack.display()
  
  # Checking if stack is empty
  print("\nIs stack empty?")
  my_stack.isEmpty()
  
  # Checking the size of the stack
  print("\nSize of the stack:")
  my_stack.size()